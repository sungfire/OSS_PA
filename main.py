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
size = [500,400]
screen = pg.display.set_mode(size)

pg.display.set_caption("Infinite_stairs")

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

