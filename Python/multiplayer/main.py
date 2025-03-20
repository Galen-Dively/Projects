import sys
import socket

def client():
    server_address = "127.0.0.1"
    port = 4444

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_address, port))
        while True:
            s.sendall("Hello server".encode("utf-8"))
            data = s.recv(1024)
            print(data.decode("utf-8"))


def server():
    address = "127.0.0.1" # will be ip address of server 
    port = 4444 # port server uses

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((address, port))

    s.listen(2) # begin listening for clients to connects
    conn, addr = s.accept()
    with conn:
        print(f"Connected to {addr}")
        while True:
            data = conn.recv(1024)
            print(data.decode("utf-8"))
            conn.sendall(data)




# check for client/server flag
match sys.argv[1]:
    case "c":
        client()
    case "s":
        server()