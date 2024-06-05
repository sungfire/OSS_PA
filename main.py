# import library
import pygame as pg
import random

# initialize the game engine
pg.init()

# define color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# set the size of screen & display screen
width = 600
height = 800
size = [width, height]
screen = pg.display.set_mode(size)

# set the initial score
high_score = 0
score = 0

# Timer settings
start_ticks = 0  # Initial timer value
time_limit = 5  # 3 seconds time limit

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
        self.direction = 0  # right = 0, left = 1
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
        self.image = pg.transform.scale(stair_image, (120, 20))
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
y = 660
for i in range(9):
    random_num = random.choice([1, -1])
    stair = Stair(x, y)
    stairs.add(stair)
    all_sprites.add(stair)
    x += random_num * 120
    if x < 0:
        x += 240
    elif x >= width:
        x -= 240
    y -= 80


# add new stair at left or right of top stair
def add_new_stair():
    global x
    global y
    random_num = random.choice([1, -1])
    new_stair = Stair(x, y)
    x += random_num * 120
    if x < 0:
        x += 240
    elif x >= width:
        x -= 240
    stairs.add(new_stair)
    all_sprites.add(new_stair)


def init_game():
    global player
    global all_sprites
    global stairs
    global start_ticks
    player = Player()
    all_sprites = pg.sprite.Group()
    all_sprites.add(player)
    stairs = pg.sprite.Group()
    x = 240
    y = 660
    for i in range(9):
        random_num = random.choice([1, -1])
        stair = Stair(x, y)
        stairs.add(stair)
        all_sprites.add(stair)
        x += random_num * 120
        if x < 0:
            x += 240
        elif x >= width:
            x -= 240
        y -= 80
    start_ticks = 0  # Reset timer


# Font settings
font = pg.font.SysFont('Arial', 24)

# Start the Loop of game
done = False
clock = pg.time.Clock()
game_started = False  # Game start flag

while not done:
    clock.tick(30)

    # Handle event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and game_started:
                player.change_direction()
            elif event.key == pg.K_LSHIFT:
                if not game_started:
                    game_started = True
                    start_ticks = pg.time.get_ticks()  # Start timer
                player.move()
                add_new_stair()
                for stair in stairs:
                    stair.update()
                score += 1
                start_ticks = pg.time.get_ticks()  # Reset timer when player moves
            elif event.key == pg.K_RSHIFT:
                init_game()
                if score > high_score:
                    high_score = score
                score = 0
                game_started = False  # Stop the game

    # Timer calculation
    if game_started:
        seconds = time_limit - (pg.time.get_ticks() - start_ticks) / 1000  # Convert to seconds
        if seconds <= 0:
            init_game()
            if score > high_score:
                high_score = score
            score = 0
            game_started = False  # Stop the game
    else:
        seconds = time_limit  # Display full time limit if game hasn't started

    # Clear screen
    screen.fill(WHITE)

    all_sprites.draw(screen)

    # Render score and timer
    score_text = font.render(f'Score: {score}', True, BLACK)
    high_score_text = font.render(f'High Score: {high_score}', True, BLACK)
    timer_text = font.render(f'Time: {seconds:.2f}', True, BLACK)
    controls_text1 = font.render('space_bar : change direction', True, BLACK)
    controls_text2 = font.render('left_shift : move', True, BLACK)

    screen.blit(score_text, (10, height - 60))
    screen.blit(high_score_text, (10, height - 30))
    screen.blit(timer_text, (10, height - 90))
    screen.blit(controls_text1, (width - controls_text1.get_width() - 10, height - 60))
    screen.blit(controls_text2, (width - controls_text2.get_width() - 10, height - 30))

    pg.display.flip()

pg.quit()
