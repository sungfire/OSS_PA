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
height = 800
size = [width, height]
screen = pg.display.set_mode(size)

pg.display.set_caption("Infinite_stairs")

player_image = pg.image.load('image/image.jpg')
stair_image = pg.image.load('image/stair.jpg')

# set player class
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(player_image, (80, 120))
        self.rect = self.image.get_rect()
        self.original_image = self.image
        self.rect.center = (width // 2, height - 200)
        self.direction = 0 #right = 0, left = 1
        self.speed = 120

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


# set stair class
class Stair(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(stair_image, (120,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 80
        if self.rect.top > height:
            self.kill()

# init sprite
player = Player()
all_sprites = pg.sprite.Group()
all_sprites.add(player)
stairs = pg.sprite.Group()

# init stairs
x = 240
y = 680
for i in range(9):
    random_num = random.choice([1, -1])
    stair = Stair(x, y)
    stairs.add(stair)
    all_sprites.add(stair)
    x += random_num*120
    if x < 0:
        x += 240
    elif x >= width:
        x -= 240
    y -= 80

def add_new_stair():
    global x
    global y
    random_num = random.choice([1, -1])
    new_stair = Stair(x, y)
    x += random_num*120
    if x < 0:
        x += 240
    elif x >= width:
        x -= 240
    stairs.add(new_stair)
    all_sprites.add(new_stair)
    

# Start the Loop of game
done = False
clock = pg.time.Clock()

while not done:
    clock.tick(30)

    # Handle event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.change_direction()
            elif event.key == pg.K_LSHIFT:
                player.move()
                add_new_stair()
                for stair in stairs:
                    stair.update()
                

    # update stairs status           
    

    # Clear screen
    screen.fill(WHITE)

    all_sprites.draw(screen)

    pg.display.flip()

