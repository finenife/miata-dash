import pygame
import socket
import pickle
import select
from pygame.locals import *
from gas.GasGauge import GasGauge
from coolant.CoolGauge import CoolantGauge
from battery.VBatGauge import VbatGauge
from rpm.RpmGauge import RpmGauge
from boost.BoostGauge import BoostGauge
from Speedometer.SpeedGauge import SpeedGauge

#setup listening port
HOST = "localhost"
PORT = 8000

#setup pygame
pygame.init()
screen = pygame.display.set_mode((800, 480))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Import Test")

# This may get added to a config file and make this some generic disp server
#fuel gauge
gas = GasGauge(20, 247) #( 671, 247)

#coolant gauge
cool = CoolantGauge(671, 247) #( 671, 247)

#battery gauge
bat = VbatGauge(671, 60)

#rpm gauge
rpm = RpmGauge(0, 0)

#boost gauge
boost = BoostGauge(22, 60)

#SPEEDOMETER
spd = SpeedGauge(300, 185, 533, 222)

#default frames dictionary
frames = {
    "fuel": 0,
    "coolant": 0,
    "bat": 0,
    "rpm": 0,
    "boost": 0,
    "speed": 0
    }

#gui loop
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        #conn.setblocking(0)
        print('Connected by', addr)
        done = False
        while not done:
                conn.send(b"up")
                packet = conn.recv(4096)
                #data.append(packet)
                #frames = pickle.loads(b"".join(data))
                frames = pickle.loads(packet)
                #if not data:
                        #break
                #print("Received:" + pickle.loads(data))
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                screen.fill((0, 0, 0))
                rpm.show(screen)
                gas.show(screen)
                cool.show(screen)
                bat.show(screen)
                boost.show(screen)
                spd.show(screen)

                pygame.display.flip()

                clock.tick(30)
