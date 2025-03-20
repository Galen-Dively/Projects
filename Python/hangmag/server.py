from concurrent.futures import thread
import socket
import threading
import packets
import pickle

class Server:
    def __init__(self, phrase):
        self.host = "127.0.0.1"
        self.port = 4444

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket fd
        self.phrase = phrase
        
        self.s.bind((self.host, self.port))
        self.s.listen()


    def start(self):
        while True:
            conn, addr = self.s.accept()
            with conn:
                print(f"Connected {addr}")
                data = conn.recv(1024) # recive 1024 bytes of data
                if not data:
                    # if no data is recvieved go to nect iteration
                    continue
                self.handle_recveived_packet(data, conn)

    def threaded_start(self):
        start_thread = threading.Thread(target=self.start)
        start_thread.start()


    def handle_recveived_packet(self, data, conn):
        decoded = pickle.loads(data)
        if isinstance(decoded, packets.Packet):
            if decoded.id == packets.PacketID.HELLO:
                print("Server hello recieved")
                phrase_packet = packets.Packet(packets.PacketID.PHRASE, self.phrase)
                encoded_phrase_packet = pickle.dumps(phrase_packet)
                conn.sendall(encoded_phrase_packet)
                
# https://realpython.com/python-sockets/