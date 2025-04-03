import socket # used for send and receiving through socket
import pickle # used for serializing data before and after transfer over network
from network.network import NetworkState, Packet, PacketID, MessageTypes

class Server:
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname()) # gets host ip address
        self.port = 5555 # port must be above 1024
        self.BUFFERSIZE = 1024 # the amount of data we accept to recieve 

        self.state = NetworkState.OFF

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Use IPv4 and TCP sock stream
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.sock.bind((self.host, self.port)) # Bind the ip and port to socket

    def start(self):
        self.state = NetworkState.WAITING
        print("Waiting for Connections: ")
        self.sock.listen() # begin listeing to connection on port 5555
        conn, addr = self.sock.accept()
        self.loop(conn, addr)


    def loop(self, conn, addr):
        self.print_server_message(MessageTypes.MESSAGE, f"{addr} connected!")
        while True:
            # Try to receive data from server
            raw_data = conn.recv(self.BUFFERSIZE)
            if not raw_data:
                self.print_server_message(MessageTypes.ERROR, "Client disconnected")
                break
            data = pickle.loads(raw_data)
            data_to_send = self.handle_data(data)
            raw_data_to_send = pickle.dumps(data_to_send)
            conn.send(raw_data_to_send)


    def print_server_message(self, type: MessageTypes, msg: str):
        if type == MessageTypes.ERROR:
            print(f"[ERROR] {msg}")
        if type == MessageTypes.MESSAGE:
            print(f"[MESSAGE] {msg}")


    def handle_data(self, data):
        if data.id == PacketID.CLIENT_HELLO:
           print("Hello")
           return Packet(PacketID.SERVER_HELLO, "Hello")
        
    def send_move(self, pos):
        move_str = ""
        for num in pos:
            move_str += str(num) + " "
        move_packet = Packet(PacketID.PLAYER_MOVE, move_str)

