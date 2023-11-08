from tkinter import *
from tkinter import ttk
from controlClient import Client
from controlClient import DataModel

class ControlPanel:

    def __init__(self, root, host='local', port=8049):
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
        # Set the geometry of the root window to be Full Screen
        root.geometry(f'{root.winfo_screenwidth()-10}x{root.winfo_screenheight()}')

        # Configure Root Bindings for Universal Control
        root.bind('<Escape>', self.exitWindow)

        # Create the main frame
        mainframe = ttk.Frame(root, padding='5')

    def exitWindow(self, *args):
        """Close the Control Panel Window Using Escape Key"""
        self.client.send_command('exit')
        self.client.close()
        root.quit()

    def update_data(self):
        """
        This will be a function that constantly takes in data from the server
        and processes the data that we just received

        Considering this, it will be an infinite loop within a thread of the gui
        """
        while True:
            json_data = self.client.receive_data()
            self.data_model.process_data(json_data)
    
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
        # Update the labels with the data from the data model
        # !!!Need to update the labels with the data from the data model!!!
        pass

root = Tk()

ControlPanel(root)

root.mainloop()
