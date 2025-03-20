import socket
import pickle


class Server:
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname()) # automatically uses your ip address as host
        self.port = 4444

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))

    def start(self):
        self.s.listen()
        conn, addr = self.s.accept()
        while True:
            pass


    def threaded_start(self):
        pass