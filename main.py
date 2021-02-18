import pygame
import generate
import level_loader
import camera
import tile

pygame.init()


window_size = (800, 800)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Window")

running = True

level = generate.makeWorld(generate.make_world(), 1)

tiles = []

camGroup = pygame.sprite.Group()

tile_group = pygame.sprite.Group()

def makeTile(tile_data):
    for t in tile_data:
        if t:
            tile_group.add(tile.tile(t[0][0]*50, t[0][1]*50, (50,50), screen, pygame.Surface((0,0))))
makeTile(level)

print(level)
camdx = 0
camdy = 0

myCamera = camera.Camera(0,0,screen)
myLevel = level_loader.level(tile_group, myCamera)
camGroup.add(myCamera)

while running:
    screen.fill((255, 255, 255))
    myCamera.x = myCamera.x + camdx
    myCamera.y = myCamera.y + camdy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                camdx = camdx + 1
            if event.key == pygame.K_RIGHT:
                camdx = camdx - 1
            if event.key == pygame.K_UP:
                camdy = camdy + 1
            if event.key == pygame.K_DOWN:
                camdy = camdy - 1
        if event.type == pygame.KEYUP:
            camdx = 0
            camdy = 0
    myLevel.render(window_size)
    myCamera.update()
    pygame.display.update()

