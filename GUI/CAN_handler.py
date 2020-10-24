import socket
import pickle
import select
import random
from time import sleep

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 8000      # Port to listen on (non-privileged ports are > 1023)

frames = {
    "fuel": 0,
    "cool": 0,
    "bat": 0,
    "rpm": 0,
    "bost": 0,
    "sped": 0
    }
data = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #print("Connected!")
    s.setblocking(0)
    #s.sendall(b'Start')
    while True:
        #print("read")
        ready = select.select([s],[],[],0)
        if ready[0]:
            data = s.recv(10)
            #print(data)
        if data == b"up":
            s.send(pickle.dumps(frames))
            #print("sent")
            data=""
        frames["fuel"]= random.randrange(0, 15)
        frames["cool"]= random.randrange(0, 15)
        frames["bat"]= random.randrange(0, 15)
        frames["rpm"]= random.randrange(0, 61)
        frames["bost"]= random.randrange(0, 15)
        frames["sped"]= random.randrange(0, 150)
