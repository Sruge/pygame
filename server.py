import socket
from _thread import *
import pickle
from information import Information
import random

server = "192.168.122.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for a connection, Server Started")
players = []


def threaded_client(conn, count):
    global players
    # info = Information(count, random.randint(40, 760), random.randint(40, 560))
    # players.append(info)
    info = Information(count, random.randint(50, 500), random.randint(50, 300))
    print("sending {}".format(info.id))
    conn.send(pickle.dumps(info))
    players.append(info)
    print(info.id, info.posX, info.posY)
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[data.id] = data
            if not data:
                print("Disconnected")
                break
            else:
                reply = players
                print("Received: ", data)
                #print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
