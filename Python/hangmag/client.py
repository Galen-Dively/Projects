import socket
from struct import pack
import packets
import pickle
import threading

class Client:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 4444

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket fd
        self.phrase = ""


    def connection(self):
        self.s.connect((self.host, self.port))
        self.s.sendall(pickle.dumps(packets.Packet(packets.PacketID.HELLO, "")))
        while True:
            data = self.s.recv(1028)
            if not data:
                continue
            self.handle_recveived_packet(data)

    def handle_recveived_packet(self, data):
        decoded = pickle.loads(data)
        if isinstance(decoded, packets.Packet):
            if decoded.id == packets.PacketID.PHRASE:
                print("Server sent phrase")
                print(decoded.payload)
                self.phrase = decoded.payload

    def send_packet(self, packet):
        data = pickle.dumps(packet)
        self.s.send(data)

# https://realpython.com/python-sockets/