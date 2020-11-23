import pygame
import os

# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

a_enemy_runner = []
path = "../assets/enemy_runner/"
files = os.listdir(path)
for f in files:
    temp = pygame.image.load(path + f)
    temp.set_colorkey((255,255,255))
    a_enemy_runner.append(temp)


a_enemy_bommer = []
path = "../assets/enemy_boommer/"
files = os.listdir(path)
for f in files:
    temp = pygame.image.load(path + f)
    temp.set_colorkey((255,255,255))
    a_enemy_bommer.append(temp)
    
class Enemy():
    def __init__(self, x, speed, kind):
        self.x = x
        self.speed = speed
        self.kind = kind
        self.i = 0

    def update(self, screen):
        self.i += 1
        if self.kind == 1:
            self.x -= self.speed
            if self.i <= len(a_enemy_runner) -1:
                screen.blit(a_enemy_runner[self.i], (self.x, 100))
            else:
                self.i = 0
        if self.kind == 2:
            if self.i <= len(a_enemy_bommer) -1:
                screen.blit(a_enemy_bommer[self.i], (self.x, 100))
            else:
                self.i = 0


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

Enemies = [Enemy(1000, 3, 1), Enemy(700, 3, 2)]

floting_giy = pygame.image.load("../assets/floting_giy.gif")
floting_giy.set_colorkey((255,255,255))
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

    screen.blit(floting_giy, (300, 100))
    
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

    for enemy in Enemies:
        enemy.update(screen)
    

    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(50)
    pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()))
