import socket
import pickle
import select
import random
import can
import math
import struct
from time import sleep

def Arb360(data):
    #can data field is byte-array
    frames["rpm"]=61-min(61,math.floor(struct.unpack_from("H", data, 0)[0]*(61/9000))) # determines RPM png max rpm 9000
    frames["bost"]=min(15,math.floor(struct.unpack_from("H", data, 2)[0]*0.0145)) # determines boost png max boost 15

def Arb372(data):
    #can data field is byte-array
    frames["bat"]=min(20,math.floor(struct.unpack_from("H", data, 2)[0]*(1.5/20))) # determines boost png max bat 20V

def Arb3E0(data):
    #can data field is byte-array
    frames["cool"]=math.floor(max(0,min(300,math.floor((((struct.unpack_from("H", data, 0)[0]*0.1)-273.15)*1.8)+32)))*(15/300)) # determines boost png max cool 300


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
        if data == b"up":
            s.send(pickle.dumps(frames))
            data=""
        for msg in bus:
            if hex(msg.arbitration_id) in ID
                ID[hex(msg.arbitration_id)](msg.data)

                
        frames["fuel"]= random.randrange(0, 15)
        frames["cool"]= random.randrange(0, 15)
        frames["bat"]= random.randrange(0, 15)
        frames["rpm"]= random.randrange(0, 61)
        frames["bost"]= random.randrange(0, 15)
        frames["sped"]= random.randrange(0, 150)
