import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 8000      # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Start')
    
    for i in range(0,10000):
        data = bytes(str(i), encoding='utf8')
        print(data)
        s.sendall(data)
    data = s.recv(1024)

print('Received', repr(data))
