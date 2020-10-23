import socket
import pickle
import select

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 8000      # Port to listen on (non-privileged ports are > 1023)

frames = {
    "fuel": 0,
    "coolant": 0,
    "bat": 0,
    "rpm": 0,
    "boost": 0,
    "speed": 0
    }
data = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.setblocking(0)
    #s.sendall(b'Start')
    while True:
        print("read")
        ready = select.select([s],[],[],0)
        if ready[0]:
            data = s.recv(10)
            print(data)
        if data == b"up":
            s.send(pickle.dumps(frames))
            print("sent")
            data=""

