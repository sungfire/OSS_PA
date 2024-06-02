# import library
import pygame as pg
import random

#initialize the game engine
pg.init()

# define color
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0, 0, 255)
GREEN = (0, 255 , 0)
RED = (255, 0, 0)

# set the size of screen & display screen
width = 600
height = 900
size = [width, height]
screen = pg.display.set_mode(size)

pg.display.set_caption("Infinite_stairs")

player_image = pg.image.load('image/image.jpg')

# set player class
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(player_image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - 60)
        self.direction = 0 #left = 0, right = 1
        self.speed = 30

# Start the Loop of game
done = False
clock = pg.time.Clock()

while not done:
    clock.tick(30)

    # Handle event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    # Clear screen
    screen.fill(BLACK)

    pg.display.flip()

