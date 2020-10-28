import pygame
from time import sleep
import socket
from icons import *
from errors import *
import math
from gas.GasGauge import GasGauge
from coolant.CoolGauge import CoolantGauge
from battery.VBatGauge import VbatGauge
from rpm.RpmGauge import RpmGauge
from boost.BoostGauge import BoostGauge
from Speedometer.SpeedGauge import SpeedGauge

class Fade(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.display.get_surface().get_rect()
        self.image = pygame.Surface(self.rect.size, flags=pygame.SRCALPHA)
        self.alpha = 255
        self.direction = 3
        
    def update(self, events):
        self.image.fill((0, 0, 0, self.alpha))
        if self.alpha == 0:
            return 1
        else: self.alpha -= self.direction

class Intro:
	def __init__(self, left_posx, left_posy, right_posx, right_posy):
		self.left_posx = left_posx
		self.left_posy = left_posy
		self.right_posx = right_posx
		self.right_posy = right_posy
		self.image = pygame.image.load('logo.png')
		self.image_left = pygame.image.load('left_logo.png')
		self.image_right = pygame.image.load('right_logo.png')
	def show_whole(self, screen):
 		screen.blit(self.get_image(), self.get_left_pos())
	def get_image(self):
		return self.image
	def get_left_image(self):
		return self.image_left
	def get_left_pos(self):
		return (self.left_posx, self.left_posy)
	def set_left_x(self, newx):
		self.left_posx = newx
	def set_left_y(self, newy):
		self.left_posy = newy
	def get_right_image(self):
		return self.image_right
	def get_right_pos(self):
		return (self.right_posx, self.right_posy)
	def set_right_x(self, newx):
		self.right_posx = newx
	def set_right_y(self, newy):
		self.right_posy = newy
	def show(self, screen):
		screen.blit(self.get_left_image(), self.get_left_pos())
		screen.blit(self.get_right_image(), self.get_right_pos())


            
def main():
    #setup main objects and pygame stuff
    pygame.init()
    screen = pygame.display.set_mode((800, 480))
    pygame.mouse.set_visible(False)
    
    #this creates the fade in for the intro maybe need to redo this
    sprites = pygame.sprite.Group(Fade())
    clock = pygame.time.Clock()

    #load generated background for alignment
    #bg=pygame.image.load('icon attempt 1.png')

    #show logo on intro
    logo = Intro(296, 150, 296+104, 150)
    logo.show_whole(screen)

    #load all icons
    leftTurn = LeftTurnSignal(136, 76)
    rightTurn = RightTurnSignal(600, 76)
    upDown = LightsUpDown(335, 70)
    brights= Brights(400, 78)
    gasLight = GasLight(255, 318)
    checkEngine = CheckEngine(222, 362)
    chargeLight = ChargeLight(277, 362)
    parking = ParkingLight(222, 406)
    commLight = CommunicationLight(277, 414)

    #load all gauges
    gas = GasGauge(20, 247) #( 671, 247)
    cool = CoolantGauge(671, 60) #( 671, 247)
    bat = VbatGauge(671, 247)
    rpm = RpmGauge(0, 30)
    boost = BoostGauge(22, 60)
    spd = SpeedGauge(300, 215, 533, 252)

    #default gauge frames dictionary
    frames = {
            "fuel": 0,
            "cool": 0,
            "bat": 0,
            "rpm": 0,
            "bost": 0,
            "sped": 0
            }
    #setup listening port
    HOST = "localhost"
    PORT = 8000
    #load all error messages
    intSer = InternalServer(50, 150)

    #intro: load logo
    pygame.display.flip()

    #intro: show logo
    sleep(2)

    #intro: this is the logo split sequence
    for i in range(0,45):
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        logo.show(screen)
        logo.set_left_x(296-i*8)
        logo.set_right_x(400+i*8)
        pygame.display.flip()
        clock.tick(60)

    #setup for intro flashings
    intro_flash_counter = 0
    show = 1
    show_add = 1
    rpm_counter = 0
    rpm_frame = 61
    other_frame = 0
    grow = -1
    other_grow = 1
    other_counter = 0
    while intro_flash_counter < 276:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            
        #intro: move gauges
        intro_flash_counter += 1
        
        sprites.update(events)
        #intrp: update rpm and other gauge values
        if intro_flash_counter > 60 and intro_flash_counter < 246:
            rpm_counter += 1
            other_counter += 1
            if rpm_counter == 3:
                rpm_frame += grow
                rpm.set_frame(rpm_frame)
                rpm_counter=0
            if other_counter == 6:
                other_frame += other_grow
                if other_frame == 15:
                    other_grow *= -1
                if other_frame <= 0:
                    other_frame = 0
                gas.set_frame(other_frame)
                cool.set_frame(other_frame)
                bat.set_frame(other_frame)
                boost.set_frame(other_frame)
                other_counter = 0
        if intro_flash_counter > 256:
            rpm.set_frame(61)
        rpm.show(screen)
        gas.show(screen)
        cool.show(screen)
        bat.show(screen)
        boost.show(screen)
        spd.show(screen)
        
        #intro: flash icons
        #print(intro_flash_counter, intro_flash_counter % 100)
        if intro_flash_counter < 150:
            leftTurn.show(screen)    
            rightTurn.show(screen)
            upDown.show(screen)
            brights.show(screen)
            gasLight.show(screen)
            checkEngine.show(screen)
            chargeLight.show(screen)
            parking.show(screen)
            commLight.show(screen)
        elif intro_flash_counter < 175:
            leftTurn.hide(screen)
            rightTurn.show(screen)
            upDown.show(screen)
            brights.show(screen)
            gasLight.show(screen)
            checkEngine.show(screen)
            chargeLight.show(screen)
            parking.show(screen)
            commLight.show(screen)
        elif intro_flash_counter < 200:
            leftTurn.hide(screen)
            rightTurn.hide(screen)
            upDown.hide(screen)
            brights.show(screen)
            gasLight.show(screen)
            checkEngine.show(screen)
            chargeLight.show(screen)
            parking.show(screen)
            commLight.show(screen)
        elif intro_flash_counter < 225:
            leftTurn.hide(screen)
            rightTurn.hide(screen)
            upDown.hide(screen)
            brights.hide(screen)
            gasLight.hide(screen)
            checkEngine.show(screen)
            chargeLight.show(screen)
            parking.show(screen)
            commLight.show(screen)
        elif intro_flash_counter < 250:
            leftTurn.hide(screen)
            rightTurn.hide(screen)
            upDown.hide(screen)
            brights.hide(screen)
            gasLight.hide(screen)
            checkEngine.show(screen)
            chargeLight.hide(screen)
            parking.hide(screen)
            commLight.show(screen)
        elif intro_flash_counter < 275:
            leftTurn.hide(screen)
            rightTurn.hide(screen)
            upDown.hide(screen)
            brights.hide(screen)
            gasLight.hide(screen)
            checkEngine.hide(screen)
            chargeLight.hide(screen)
            parking.hide(screen)
            commLight.show(screen)
        commLight.show(screen)
        sprites.draw(screen)
        pygame.display.update()
        clock.tick(60)
    print("done")
    rpm.set_frame(61)
    rpm.show(screen)
    commLight.show(screen)
    gas.show(screen)
    cool.show(screen)
    bat.show(screen)
    boost.show(screen)
    spd.show(screen)
    #intSer.show(screen)
    pygame.display.update()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("listening")
        s.bind((HOST, PORT))
        s.settimeout(2)
        s.listen()
        try:
            conn, addr = s.accept()
        except:
            intSer.show(screen)
            pygame.display.update()
            return
        with conn:
            commLight.hide(screen)
            print('Connected by', addr)
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
             
if __name__ == '__main__':
    main()
