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

root = Tk()

ControlPanel(root)

root.mainloop()
