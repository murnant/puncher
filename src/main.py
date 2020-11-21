import pygame
import os

# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

punching = False
a_punch = []
i = 0
path = "../assets/punch/"
files = os.listdir(path)
for f in files:
    temp = pygame.image.load(path + f)
    temp.set_colorkey((255,255,255))
    a_punch.append(temp)
    

# ***************** Loop Land Below *****************
# Everything under 'while running' will be repeated over and over again
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    screen.fill((0,0,0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        punching = True
        
    if punching:
        i += 1
    if i <= len(a_punch) -1:
        screen.blit(a_punch[i], (100, 100))
    else:
        i = 0
        punching = False
    

    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(5)
    pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()))
