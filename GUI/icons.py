import pygame

class LeftTurnSignal:
        def __init__(self, posx, posy):
            self.posx = posx
            self.posy = posy
            self.image = pygame.image.load('left_turn.png')
            self.rect = pygame.image.load('left_turn.png')
            self.rect.fill((0,0,0))
            
        def get_image(self):
            return self.image
        def get_pos(self):
            return (self.posx, self.posy)
        def show(self, screen):
                self.rect.set_alpha(0)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                
        def hide(self, screen):
                self.rect.set_alpha(255)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
               
                
class RightTurnSignal:
        def __init__(self, posx, posy):
            self.posx = posx
            self.posy = posy
            self.image = pygame.image.load('right_turn.png')
            self.rect = pygame.image.load('right_turn.png')
            self.rect.fill((0,0,0))
            
        def get_image(self):
            return self.image
        def get_pos(self):
            return (self.posx, self.posy)
        def show(self, screen):
                self.rect.set_alpha(0)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                
        def hide(self, screen):
                self.rect.set_alpha(255)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                

class LightsUpDown:
        def __init__(self, posx, posy):
            self.posx = posx
            self.posy = posy
            self.image = pygame.image.load('headlights_up_down.png')
            self.rect = pygame.image.load('headlights_up_down.png')
            self.rect.fill((0,0,0))
            self.transparent=0
        def get_image(self):
            return self.image
        def get_pos(self):
            return (self.posx, self.posy)
        def show(self, screen):
                self.rect.set_alpha(0)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent=0
        def hide(self, screen):
                self.rect.set_alpha(self.transparent)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent += 25

class Brights:
        def __init__(self, posx, posy):
            self.posx = posx
            self.posy = posy
            self.image = pygame.image.load('brights.png')
            self.rect = pygame.image.load('brights.png')
            self.rect.fill((0,0,0))
            self.transparent=0
        def get_image(self):
            return self.image
        def get_pos(self):
            return (self.posx, self.posy)
        def show(self, screen):
                self.rect.set_alpha(0)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent=0
        def hide(self, screen):
                self.rect.set_alpha(self.transparent)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent += 25

class GasLight:
        def __init__(self, posx, posy):
            self.posx = posx
            self.posy = posy
            self.image = pygame.image.load('gas_light.png')
            self.rect = pygame.image.load('gas_light.png')
            self.rect.fill((0,0,0))
            self.transparent=0
        def get_image(self):
            return self.image
        def get_pos(self):
            return (self.posx, self.posy)
        def show(self, screen):
                self.rect.set_alpha(0)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent=0
        def hide(self, screen):
                self.rect.set_alpha(self.transparent)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent += 25
            
class CheckEngine:
        def __init__(self, posx, posy):
            self.posx = posx
            self.posy = posy
            self.image = pygame.image.load('check_engine.png')
            self.rect = pygame.image.load('check_engine.png')
            self.rect.fill((0,0,0))
            self.transparent=0
        def get_image(self):
            return self.image
        def get_pos(self):
            return (self.posx, self.posy)
        def show(self, screen):
                self.rect.set_alpha(0)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent=0
        def hide(self, screen):
                self.rect.set_alpha(self.transparent)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent += 25
            
class ChargeLight:
        def __init__(self, posx, posy):
            self.posx = posx
            self.posy = posy
            self.image = pygame.image.load('charge.png')
            self.rect = pygame.image.load('charge.png')
            self.rect.fill((0,0,0))
            self.transparent=0
        def get_image(self):
            return self.image
        def get_pos(self):
            return (self.posx, self.posy)
        def show(self, screen):
                self.rect.set_alpha(0)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent = 0
        def hide(self, screen):
                self.rect.set_alpha(self.transparent)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent += 25

class ParkingLight:
        def __init__(self, posx, posy):
            self.posx = posx
            self.posy = posy
            self.image = pygame.image.load('ebrake.png')
            self.rect = pygame.image.load('ebrake.png')
            self.rect.fill((0,0,0))
            self.transparent=0
        def get_image(self):
            return self.image
        def get_pos(self):
            return (self.posx, self.posy)
        def show(self, screen):
                self.rect.set_alpha(0)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent=0
        def hide(self, screen):
                self.rect.set_alpha(self.transparent)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent += 25

class CommunicationLight:
        def __init__(self, posx, posy):
            self.posx = posx
            self.posy = posy
            self.image = pygame.image.load('comm.png')
            self.rect = pygame.image.load('comm.png')
            self.rect.fill((0,0,0))
            self.transparent =0
        def get_image(self):
            return self.image
        def get_pos(self):
            return (self.posx, self.posy)
        def show(self, screen):
                self.rect.set_alpha(0)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent=0
        def hide(self, screen):
                self.rect.set_alpha(self.transparent)
                screen.blit(self.get_image(), self.get_pos())
                screen.blit(self.rect, self.get_pos())
                self.transparent += 25
