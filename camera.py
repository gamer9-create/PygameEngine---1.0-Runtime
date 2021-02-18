import pygame


pygame.init()

class Camera(pygame.sprite.Sprite):
    def __init__(self,x,y,screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.rendering = False
    def update(self):
        self.rendering = True

        if self.rendering == False:
            self.screen.fill((0,0,0))
