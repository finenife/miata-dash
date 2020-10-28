import pygame

class InternalServer:
        def __init__(self, posx, posy):
            self.posx = posx
            self.posy = posy
            self.image = pygame.image.load('test.png')
            self.rect = pygame.image.load('failure_to_connect_int_ser.png')
            self.hidden = True
            self.rect.fill((0,0,0))
            
        def get_image(self):
            return self.image
        def get_pos(self):
            return (self.posx, self.posy)
        def show(self, screen):
            self.hidden = False
            self.rect.set_alpha(0)
            screen.blit(self.get_image(), self.get_pos())
            screen.blit(self.rect, self.get_pos())
                
        def hide(self, screen):
            self.hidden = True
            self.rect.set_alpha(255)
            screen.blit(self.get_image(), self.get_pos())
            screen.blit(self.rect, self.get_pos())
               

