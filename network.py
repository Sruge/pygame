import socket
import pickle
from information import Information

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.122.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.playerInfo = self.connect()

    def get_player(self):
        return self.player

    def connect(self):
        try:
            self.client.connect(self.addr)
            print("Could connect")
            data = (pickle.loads(self.client.recv(2048)))
            return data
        except:
            print("Could not connect")
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
