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

# This may get added to a config file and make this some generic disp server
#fuel gauge

#coolant gauge

#battery gauge

#rpm gauge

#boost gauge

#SPEEDOMETER

#default frames dictionary
frames = {
    "fuel": 0,
    "cool": 0,
    "bat": 0,
    "rpm": 0,
    "bost": 0,
    "sped": 0
    }

#gui loop
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("listening")
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        #conn.setblocking(0)
        print('Connected by', addr)
        pygame.init()
        screen = pygame.display.set_mode((800, 480))
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("Import Test")
        gas = GasGauge(20, 247) #( 671, 247)
        cool = CoolantGauge(671, 247) #( 671, 247)
        bat = VbatGauge(671, 60)
        rpm = RpmGauge(0, 0)
        boost = BoostGauge(22, 60)
        spd = SpeedGauge(300, 185, 533, 222)
        done = False
        while not done:
                conn.send(b"up")
                packet = conn.recv(4096)
                frames = pickle.loads(packet)
                for event in pygame.event.get():
                        if event.type == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                                done = True
                screen.fill((0, 0, 0))
                rpm.set_frame(frames["rpm"])
                rpm.show(screen)
                gas.set_frame(frames["fuel"])
                gas.show(screen)
                cool.set_frame(frames["cool"])
                cool.show(screen)
                bat.set_frame(frames["bat"])
                bat.show(screen)
                boost.set_frame(frames["bost"])
                boost.show(screen)
                spd.set_speed(frames["sped"])
                spd.show(screen)

                pygame.display.flip()

                clock.tick(60)
