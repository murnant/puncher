import pygame
import os

# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

player_x = 100

punching = False
player_running = False

a_punch = []
i = 0
path = "../assets/punch/"
files = os.listdir(path)
for f in files:
    temp = pygame.image.load(path + f)
    temp.set_colorkey((255,255,255))
    a_punch.append(temp)


a_run = []
path = "../assets/run/"
files = os.listdir(path)
for f in files:
    temp = pygame.image.load(path + f)
    temp.set_colorkey((255,255,255))
    a_run.append(temp)
    
a_tap = []
path = "../assets/tap_tap/"
files = os.listdir(path)
for f in files:
    temp = pygame.image.load(path + f)
    temp.set_colorkey((255,255,255))
    a_tap.append(temp)
    

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
    if keys[pygame.K_RIGHT]:
        player_x += 3
        player_running = True
        Direction = False
    if keys[pygame.K_LEFT]:
        player_x -= 3
        player_running = True
        Direction = True
    
    
    if player_running:
        i += 1
        if i <= len(a_run) -1:
            player_pic_Direction = pygame.transform.flip(a_run[i], Direction, False)
            screen.blit(player_pic_Direction, (player_x, 100))
        else:
            i = 0
            player_running = False
    
        
    elif punching:
        i += 1
        if i <= len(a_punch) -1:
            player_pic_Direction = pygame.transform.flip(a_punch[i], Direction, False)
            screen.blit(player_pic_Direction, (player_x, 100))
        else:
            i = 0
            punching = False
    else:
        i += 1
        if i <= len(a_tap) -1:
            screen.blit(a_tap[i], (player_x, 100))
        else:
            i = 0
    

    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(50)
    pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()))
