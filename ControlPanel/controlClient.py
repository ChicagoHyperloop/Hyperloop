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

    def send_command(self, command):
        """Send a command to the server

        Args:
            command (str): The command to be sent to the server

        """
        # Working with Java server, so newline character is needed for command processing
        command += '\n'
        self.client_socket.send(command.encode('utf-8'))
        data = self.client_socket.recv(1024)
        # Terminal will print the feedback from the server (for debugging purposes)
        print('Received from server: ' + data.decode('utf-8').rstrip())

