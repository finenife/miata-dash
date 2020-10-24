import socket
import pickle
import select
import random
import can
import math
import struct

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

ID = {
    '0x360': Arb360 #1 rpm [0,1] rpm, 0.1 kPa [2,3] bost
    '0x372': Arb372 #0.1 volts [0,1] batt  
    '0x3E0': Arb3E0 #0.1 Kelvin [0,1] cool
    }

data = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.setblocking(0)
    bus = can.Bus(interface='socketcan', channel='can0')
    while True:
        ready = select.select([s],[],[],0)
        if ready[0]:
            data = s.recv(10)
            #print(data)
        if data == b"up":
            s.send(pickle.dumps(frames))
            #print("sent")
            data=""
        for msg in bus:
            if msg.arbitration_id in ID
        frames["fuel"]= random.randrange(0, 15)
        frames["cool"]= random.randrange(0, 15)
        frames["bat"]= random.randrange(0, 15)
        frames["rpm"]= random.randrange(0, 61)
        frames["bost"]= random.randrange(0, 15)
        frames["sped"]= random.randrange(0, 150)
