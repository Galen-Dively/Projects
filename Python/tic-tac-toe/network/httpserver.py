import socket
import dataclasses
import threading

@dataclasses.dataclass
class HTTPReponse:
    def __init__(self):
        self.code = 0
        self.response = 0
        self.data = 0
        self.reponse_string = f"""
        HTTP/1.1 {self.code} {self.reponse}

        {self.data}
        """
    

f = open("test.html", "wb")

http_response = b"""\
HTTP/1.1 200 OK

Hello, World, I just created a Web Server...!
    """

def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 4444))
    sock.listen()
    return sock

def handle_conn(conn):
    data = conn.recv(1024)
    print(data.decode())
    check_request(data.decode())


    conn.sendall(http_response)

    conn.close()

def check_request(data):
   split_data = data.split("\n")
   


sock = create_socket()
root = "root/"

while True:
    conn, addr = sock.accept()
    threaded_handle = threading.Thread(target=handle_conn, args=(conn,))
    threaded_handle.start()

