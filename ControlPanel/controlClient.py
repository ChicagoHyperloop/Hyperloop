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
        # Dictionary to store the data from previous update, used to track changes
        self.prevData = {}

    def process_data(self, json_data):
        """
        Update the previous data model to match current, and then
        Process the JSON data received from the server
        
        Args:
            json_data (str): The JSON data received from the server
        """
        self.prevData = self.data
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
        

    def receive_data(self):
        """
        Receive data from the server.

        Returns:
            str: The received data as a string.
        """
        # Try to receive data from the server
        try:
            ### REVISIT THIS AS MORE DATA WILL BE MORE PROGRAM INTENSIVE
            self.client_socket.settimeout(0.065)  # Set a timeout of 0.025 seconds vs server sleep of 0.070 seconds
            data = self.client_socket.recv(1024)
            print('Received from server: ' + data.decode('utf-8').rstrip()) # Get terminal feedback of data stream
            return data.decode('utf-8').rstrip()
        # If OSError occurs
        except OSError as e:
            # handle specific error
            if e.errno == 9:
                print("Socket closed...")
                return None
            else:
                print("Error while receiving data: " + str(e))
                return None
        # If socket connection timed out, return None
        except socket.timeout:
            return None
        # If socket connection was closed, return None
        except ConnectionResetError:
            print("Connection closed by the server.")
            return None
        finally:
            self.client_socket.settimeout(None)  # Reset the timeout to blocking mode


    def close_connection(self):
        """Close the client socket"""
        self.client_socket.close()
