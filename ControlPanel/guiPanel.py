### Tkinter Imports ###
import tkinter as tk
from tkinter import *
from tkinter import ttk
### Matplotlib Imports ###
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
### Threading Imports ###
import threading
from threading import Event
### Time Imports ###
import time
### Client Side Imports ###
from controlClient import Client
from controlClient import DataModel

'''
TODO: Find out what data is going to be used for the Pod, and then
      how we want to display this data in a meaningful way.
      - Work on discovering data set
      - Work on displaying data set
'''

'''
NOTE: The GUI works with the server and it works without a server connection,
      it can successfully wait for connection, however while implementing this
      some OSErrors occur but are handled, and when handled the application runs
      as supposed to in conjunction with server.
      - Just slightly annoying seeing the OSErrors popping up in the terminal.
'''

class ControlPanel:

    def __init__(self, root, host='localhost', port=8049):
        """
        Initialize the GUI
        
        Args:
            root (Tk): The root window of the GUI
            host (str): The host address of the server, default: localhost
            port (int): The port number of the server, default: 8049
        """
        # Initialize the root window and set the title
        root.title('Hyper Loop Chicago Control Pod')
        # Set the geometry of the root window to be Full Screen and Resizeable
        root.geometry(f'{root.winfo_screenwidth()-10}x{root.winfo_screenheight()}')
        root.resizable(True, True)

        # Create a Toplevel window for connection status
        self.connection_frame = ttk.Frame(root, padding='5')
        self.connection_text = StringVar()
        self.connection_label = ttk.Label(self.connection_frame, textvariable=self.connection_text)
        self.connection_label.pack()
        self.connection_frame.pack()

        # Initialize the client socket and data model
        self.client = None
        self.data_model = None

        # Create the variables needed for labels and data
        self.brake_activated = BooleanVar(value=False)
        self.brake_activated_text = StringVar(value='Off')
        self.brake_temperature = DoubleVar(value=0)
        self.speed = IntVar(value=0)

        # Create thread for constantly updating values from the server
        self.stop_event = Event()
        self.stop_event.set()

        # Create the main frame
        self.mainframe = ttk.Frame(root, padding='5')

        ### Create Labels for Displaying Data
        # Create a Brake Status Label
        brake_status_label = ttk.Label(self.mainframe, text='Brake Status')
        brake_status_label.pack(pady=10)
        brake_status_variable_label = ttk.Label(self.mainframe, textvariable=self.brake_activated_text)
        brake_status_variable_label.pack(pady=10)
        # Create a Brake Temperature Label
        brake_temperature_label = ttk.Label(self.mainframe, text='Brake Temperature')
        brake_temperature_label.pack(pady=10)
        brake_temperature_variable_label = ttk.Label(self.mainframe, textvariable=self.brake_temperature)
        brake_temperature_variable_label.pack(pady=10)
        
        # Create a Matplotlib figure and axis
        fig, ax = plt.subplots()
        self.bar = ax.bar([''], [self.brake_temperature.get()], color='skyblue')
        # ax.set_xlabel('Sources')
        ax.set_ylabel('Temperature (Celsius)')
        ax.set_title('Brake Temperature')
        ax.set_ylim(0, 200)
        # Create a Matplotlib canvas for embedding in Tkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self.mainframe)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        # Create a colormap for gradient effect
        self.cmap = LinearSegmentedColormap.from_list('custom_gradient', ['blue', 'skyblue', 'lightblue', 'white', 'yellow', 'orange', 'red', 'darkred'])
        # Set background color of canvas to be same as tkinter application
        fig.patch.set_facecolor(root.cget('bg'))
        ax.patch.set_facecolor(root.cget('bg'))

        # Create a Speed Label
        speed_label = ttk.Label(self.mainframe, text='Speed')
        speed_label.pack(pady=10)
        speed_variable_label = ttk.Label(self.mainframe, textvariable=self.speed)
        speed_variable_label.pack(pady=10)

        threading.Thread(target=self.initialize_client, args=(root, host, port), daemon=True).start()


    #############################################################
    #              INITIALIZATION FUNCTIONS
    #############################################################
    def initialize_client(self, root, host, port):
        """Initialize the client socket"""
        i = 0
        while True:
            try:
                # Attempt to initialize the client socket and data model
                self.client = Client(host, port)
                self.data_model = DataModel()
                self.client.send_command('ready')
                break
            except ConnectionRefusedError:
                self.connection_text.set('Connection Refused. Waiting for Server to Start' + ('.' * (i%4)))
                i += 1
                time.sleep(0.5)
                continue

        self.connection_text.set('Connection Successful. Starting Control Panel...')
        time.sleep(2)
        self.connection_frame.destroy()

        # Configure Root Bindings for Universal Control
        root.bind('<Escape>', self.exitWindow)
        root.bind('<space>', self.toggleBrakes)
        root.bind('<Up>', self.increaseSpeed)
        root.bind('<Down>', self.decreaseSpeed)

        # Pack the main frame
        self.mainframe.pack()

        self.stop_event.clear()
        # Create thread for constantly updating values from the server
        threading.Thread(target=self.update_data, daemon=True).start()

        root.update()


    #############################################################
    #               CONTROL/BIND FUNCTIONS
    #############################################################
    def exitWindow(self, *args):
        """Close the Control Panel Window Using Escape Key"""
        self.stop_event.set()
        remaining_data = self.client.receive_data()
        while remaining_data:
            remaining_data = self.client.receive_data()
        self.client.send_command('exit')
        self.client.close_connection()
        root.after(100, root.quit)

    def toggleBrakes(self, *args):
        """Toggle the brakes for the pod"""
        if self.brake_activated.get():
            self.client.send_command('Brakes: Off')
        else:
            self.client.send_command('Brakes: On')
    
    def increaseSpeed(self, *args):
        """Increase the speed of the pod"""
        self.client.send_command('Accelerate')

    def decreaseSpeed(self, *args):
        """Decrease the speed of the pod"""
        self.client.send_command('Decelerate')


    #############################################################
    #                   ANIMATION FUNCTIONS
    #############################################################
   

    #############################################################
    #               DATA PROCESSING FUNCTIONS
    #############################################################
    '''
    TODO: Somehow make it so that data is only updated if there is a change.
          Also, if there is a change, only update the label that changed, 
          rather than assigning all the labels to the data model values.
          Theoretically, this will make the GUI more efficient, making data
          processing much faster and a more responsive GUI. Especially when
          the GUI will start plotting data.
          Possible Data Plotting Libraries:
            - matplotlib **(Current Plan)**
            - PyQTGraph **(Very Promising)**
            - Plotly
            - PyPlot
            - Bokeh
            - Seaborn
    '''

    def update_data(self):
        """
        This will be a function that constantly takes in data from the server
        and processes the data that we just received

        Considering this, it will be an infinite loop within a thread of the gui
        """
        # Run continously until "threading" event is stopped upon exiting the GUI
        while not self.stop_event.is_set():
            received_data = self.client.receive_data()

            if not received_data or len(received_data.split('\n')) > 1:
                print('Waiting on Connection')
                continue
            # Also, only process data if actual data was received
            if received_data:
                # print('json_data: ' + received_data)
                self.process_data(received_data)
    
    def process_data(self, json_data):
        """
        Process the JSON data received from the server
        
        Args:
            json_data (str): The JSON data received from the server

        """
        self.data_model.process_data(json_data) # Updates the data model
        self.update_labels() # Updates the labels with new data in the model

    def update_labels(self):
        """Update the labels with the data from the data model"""
        self.brake_activated.set(self.data_model.data['brakes']['activated'])
        self.brake_temperature.set(self.data_model.data['brakes']['temperature'])
        self.speed.set(self.data_model.data['speed'])

        # Update the brake status text
        if self.brake_activated.get():
            self.brake_activated_text.set('On')
        else:
            self.brake_activated_text.set('Off')

        normalized_height = self.brake_temperature.get() / 200.0
        for bar_ in self.bar:
            bar_.set_height(self.brake_temperature.get())
            bar_.set_color(self.cmap(normalized_height))
        self.canvas.draw()


root = Tk()

ControlPanel(root)

root.mainloop()
