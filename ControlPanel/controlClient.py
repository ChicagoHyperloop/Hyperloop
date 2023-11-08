import socket

class Client:

    def __init__(self, host, port):
        """Initialize the client socket and connect to the server

        Args:
            host (str): The host address of the server
            port (int): The port number of the server

        """
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    