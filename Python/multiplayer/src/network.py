import socket
import pickle
from packets import *
from player import Player

class Client:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 4444

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, player):
        self.s.connect((self.host, self.port))


        # Craft first player update packet
        raw_initial_packet = PlayerUpdate(id=player.id, x=player.rect.x, y=player.rect.y, packet=1)
        serialized_packet = pickle.dumps(raw_initial_packet)

        self.s.send(serialized_packet)
    
    def recv_packet(self, player):
        data =  self.s.recv(1024)
        loaded =  pickle.loads(data)
        # print("Recived: " + str(loaded))
        # print(type(loaded))
        return loaded
    
    def send_packet(self, player):
        raw_initial_packet = PlayerUpdate(id=player.id, x=player.rect.x, y=player.rect.y, packet=1)
        serialized_packet = pickle.dumps(raw_initial_packet)
        self.s.send(serialized_packet) 
    

