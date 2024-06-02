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
width = 630
height = 900
size = [width, height]
screen = pg.display.set_mode(size)

pg.display.set_caption("Infinite_stairs")

player_image = pg.image.load('image/image.jpg')
stair_image = pg.image.load('image/stair.jpg')

# set player class
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(player_image, (30,45))
        self.rect = self.image.get_rect()
        self.original_image = self.image
        self.rect.center = (width // 2, height - 60)
        self.direction = 0 #right = 0, left = 1
        self.speed = 30

    # change direction
    def change_direction(self):
        if self.direction == 0:
            self.direction = 1
            self.image = pg.transform.flip(self.original_image, True, False)
        elif self.direction == 1:
            self.direction = 0
            self.image = self.original_image

    # make move
    def move(self):
        if self.direction == 0:
            self.rect.x += self.speed
        elif self.direction == 1:
            self.rect.x -= self.speed

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
    screen.fill(WHITE)

    pg.display.flip()

