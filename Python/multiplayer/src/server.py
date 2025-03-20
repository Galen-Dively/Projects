import socket
import threading
import pickle
import packets

class Server:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 4444

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))

        self.running = True
        self.connected_client_amt = 0
        self.connections = {}
        self.lock = threading.Lock()  # For thread-safe access to shared resources

    def server(self):
        self.server_socket.listen()
        print("Server started and listening")
        while self.running:
            conn, addr = self.server_socket.accept()
            threaded_client = threading.Thread(target=self.handle_client, args=(conn, addr))
            threaded_client.start()

    def handle_client(self, conn, addr):
        self.connected_client_amt += 1
        id = self.connected_client_amt
        self.connections[id] = conn

        print(f"Connected to {addr} (ID: {id})")

        try:
            while True:
                data = conn.recv(1024)
                # if not data:  # Client disconnected
                #     break

                # Process received data
                packet = pickle.loads(data)
                print(f"Received from {addr}: {packet}")

                # Broadcast the packet to all other clients
                for other_id, connection in self.connections.items():
                    if other_id != id:
                        try:
                                connection.sendall(data)
                        except Exception as e:
                                print(f"Failed to send data to client {other_id}: {e}")

        except Exception as e:
            print(f"Error handling client {addr}: {e}")
        finally:
            del self.connections[id]
            conn.close()
            print(f"Client {addr} (ID: {id}) disconnected")

    def stop(self):
        self.running = False
        self.server_socket.close()
        print("Server stopped")


if __name__ == "__main__":
    server = Server()
    try:
        server.server()
    except KeyboardInterrupt:
        server.stop()