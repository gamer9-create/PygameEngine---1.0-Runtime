import pygame

pygame.init()


class tile(pygame.sprite.Sprite):
    def __init__(self, x, y, size, screen, image):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.render_offset = [0, 0]
        self.group = None
        self.level_gravity = None
        self.object_gravity = 0
        self.gravity_apply = False
        self.falling = False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.image.fill((255, 0, 0))
        if self.group:
            coll = False
            for g in self.group:
                if g:
                    if self.rect.colliderect(g.rect):
                        self.falling = False
                        coll = True
            if not coll:
                self.falling = True
            else:
                self.falling = False
        if self.falling and self.gravity_apply:
            self.object_gravity = self.level_gravity
            self.y = self.y + self.object_gravity
        self.screen.blit(self.image, (self.x + self.render_offset[0], self.y + self.render_offset[1]))
