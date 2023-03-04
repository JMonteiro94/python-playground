import socket
import json


class Network:

    def __init__(self, name):
        self.name = name
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server = "localhost"
        self.port = 5500
        self.addr = (self.server, self.port)
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            self.client.sendall(self.name.encode())
            return json.loads(self.client.recv(2048))
        except Exception as e:
            self.disconnect(e)

    def send(self, data):
        try:
            self.client.send(json.dumps(data).encode())
            return json.loads(self.client.recv(2048).decode())
        except socket.error as e:
            self.disconnect(e)

    def disconnect(self, msg):
        print("[EXCEPTION] disconnected: ", msg)
        try:
            self.client.send({10: []})
        except:
            self.client.close()
        self.client.close()


n = Network("test")
print(n.send({0: []}))
