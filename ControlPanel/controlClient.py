import socket
import json

class DataModel:
    '''
    Abstract Idea for this Data Model Class:
    - This class will be used to store the data received from the server
    - The data will be stored in a dictionary
      - This way the data is easily accessible for the GUI
    - This class will also handle any change in the data from the server
    '''

    def __init__(self):
        """Initialize the data model"""
        # Dictionary to store the data received from the server
        self.data = {}

    def process_data(self, json_data):
        """
        Process the JSON data received from the server
        
        Args:
            json_data (str): The JSON data received from the server

        """
        self.data = json.loads(json_data)


class Client:

    def __init__(self, host, port):
        """
        Initialize the client socket and connect to the server

        Args:
            host (str): The host address of the server
            port (int): The port number of the server

        """
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def send_command(self, command):
        """
        Send a command to the server

        Args:
            command (str): The command to be sent to the server

        """
        # Working with Java server, so newline character is needed for command processing
        command += '\n'
        self.client_socket.send(command.encode('utf-8'))
        # data = self.client_socket.recv(1024)
        # Terminal will print the feedback from the server (for debugging purposes)
        # print('Received from server: ' + data.decode('utf-8').rstrip())

    def receive_data(self):
        """
        Receive JSON data from the server

        Returns:
            str: The JSON data received from the server

        """
        data = self.client_socket.recv(1024)
        # Terminal will print the feedback from the server (for debugging purposes)
        print('Received from server: ' + data.decode('utf-8').rstrip())
        return data.decode('utf-8').rstrip()

    def close_connection(self):
        """Close the client socket"""
        self.client_socket.close()
