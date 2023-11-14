from tkinter import *
from tkinter import ttk
import threading
from controlClient import Client
from controlClient import DataModel

class ControlPanel:

    def __init__(self, root, host='localhost', port=8049):
        """
        Initialize the GUI
        
        Args:
            root (Tk): The root window of the GUI
            host (str): The host address of the server, default: localhost
            port (int): The port number of the server, default: 8049
        """
        # Initialize the client socket and data model
        # !!!As of right now, server needs to be running first before client is created!!!
        self.client = Client(host, port)
        self.data_model = DataModel()

        # Initialize the root window and set the title
        root.title('Hyper Loop Chicago Control Pod')
        # Set the geometry of the root window to be Full Screen and Resizeable
        root.geometry(f'{root.winfo_screenwidth()-10}x{root.winfo_screenheight()}')
        root.resizable(True, True)

        # Configure Root Bindings for Universal Control
        root.bind('<Escape>', self.exitWindow)
        root.bind('<space>', self.toggleBrakes)
        root.bind('<Up>', self.increaseSpeed)
        root.bind('<Down>', self.decreaseSpeed)

        # Create the variables needed for labels and data
        self.brake_activated = BooleanVar(value=False)
        self.brake_activated_text = StringVar(value='Off')
        self.brake_temperature = IntVar(value=0)
        self.speed = IntVar(value=0)

        # Create thread for constantly updating values from the server
        data_thread = threading.Thread(target=self.update_data, daemon=True)
        data_thread.start()

        # Create the main frame
        mainframe = ttk.Frame(root, padding='5')

        ### Create Labels for Displaying Data
        # Create a Brake Status Label
        brake_status_label = ttk.Label(mainframe, text='Brake Status')
        brake_status_label.pack(pady=10)
        brake_status_variable_label = ttk.Label(mainframe, textvariable=self.brake_activated_text)
        brake_status_variable_label.pack(pady=10)
        # Create a Brake Temperature Label
        brake_temperature_label = ttk.Label(mainframe, text='Brake Temperature')
        brake_temperature_label.pack(pady=10)
        brake_temperature_variable_label = ttk.Label(mainframe, textvariable=self.brake_temperature)
        brake_temperature_variable_label.pack(pady=10)
        # Create a Speed Label
        speed_label = ttk.Label(mainframe, text='Speed')
        speed_label.pack(pady=10)
        speed_variable_label = ttk.Label(mainframe, textvariable=self.speed)
        speed_variable_label.pack(pady=10)

        # Pack the main frame
        mainframe.pack()


    #############################################################
    #               CONTROL/BIND FUNCTIONS
    #############################################################
    def exitWindow(self, *args):
        """Close the Control Panel Window Using Escape Key"""
        self.client.send_command('exit')
        self.client.close()
        root.quit()

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
    #               DATA PROCESSING FUNCTIONS
    #############################################################
    def update_data(self):
        """
        This will be a function that constantly takes in data from the server
        and processes the data that we just received

        Considering this, it will be an infinite loop within a thread of the gui
        """
        while True:
            json_data = self.client.receive_data()
            self.process_data(json_data)
    
    def process_data(self, json_data):
        """
        Process the JSON data received from the server
        
        Args:
            json_data (str): The JSON data received from the server

        """
        self.data_model.process_data(json_data)
        self.update_labels()

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


root = Tk()

ControlPanel(root)

root.mainloop()
