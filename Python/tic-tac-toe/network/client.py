import socket
import pickle
from network.network import PacketID, Packet, Payload


class Client:
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname()) # gets host ip address
        self.port = 5555 # port must be above 1024

        self.BUFFERSIZE = 1024 # the amount of data we accept to recieve 

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Use IPv4 and TCP sock stream

        self.stage = 0

    def connect(self):
        self.sock.connect((self.host, self.port))
        data = pickle.dumps(Packet(PacketID.CLIENT_HELLO, Payload("hello")))
        self.sock.send(data)
        data = self.recv_packet()
        if data.id == PacketID.SERVER_HELLO:
            print("Server is ready")
        else:
            print("Server did not say hello")
        

        
        

    def recv_packet(self):
        return pickle.loads(self.sock.recv(1024))


    def send_move(self, pos: list[int]):
        move_str = ""
        for num in pos:
            move_str += str(num) + " "
        move_packet = Packet(PacketID.PLAYER_MOVE, move_str)
        self.sock.send(pickle.dumps(move_packet))
