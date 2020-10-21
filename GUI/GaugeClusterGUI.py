import pygame
from pygame.locals import *
from gas.GasGauge import GasGauge
from coolant.CoolGauge import CoolantGauge
from battery.VBatGauge import VbatGauge
from rpm.RpmGauge import RpmGauge
from boost.BoostGauge import BoostGauge
from Speedometer.SpeedGauge import SpeedGauge

#setup pygame
pygame.init()
screen = pygame.display.set_mode((800, 480))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Import Test")

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

#gui loop
done = False
while not done:
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
