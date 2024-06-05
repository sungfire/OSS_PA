# import library
import pygame as pg
import random

# initialize the game engine
pg.init()

# define color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 150)
GREEN = (0, 150, 0)
RED = (150, 0, 0)

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
time_limit = 3  # 3 seconds time limit

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
last_stair_x = x  # Track the x coordinate of the last stair
for i in range(9):
    stair = Stair(last_stair_x, y)
    stairs.add(stair)
    all_sprites.add(stair)
    random_num = random.choice([1, -1])
    last_stair_x += random_num * 120
    if last_stair_x < 0:
        last_stair_x += 240
    elif last_stair_x >= width:
        last_stair_x -= 240
    y -= 80

# add new stair at left or right of top stair
def add_new_stair():
    global last_stair_x
    global y
    random_num = random.choice([1, -1])
    new_stair = Stair(last_stair_x, y)
    last_stair_x += random_num * 120
    if last_stair_x < 0:
        last_stair_x += 240
    elif last_stair_x >= width:
        last_stair_x -= 240
    stairs.add(new_stair)
    all_sprites.add(new_stair)

def init_game():
    global player
    global all_sprites
    global stairs
    global start_ticks
    global time_limit
    global game_started
    global game_over
    global last_stair_x
    player = Player()
    all_sprites = pg.sprite.Group()
    all_sprites.add(player)
    stairs = pg.sprite.Group()
    x = 240
    y = 660
    last_stair_x = x  # Reset the x coordinate of the last stair
    for i in range(9):
        stair = Stair(last_stair_x, y)
        stairs.add(stair)
        all_sprites.add(stair)
        random_num = random.choice([1, -1])
        last_stair_x += random_num * 120
        if last_stair_x < 0:
            last_stair_x += 240
        elif last_stair_x >= width:
            last_stair_x -= 240
        y -= 80
    start_ticks = 0  # Reset timer
    time_limit = 3  # Reset time limit
    game_started = False  # Game start flag
    game_over = False # Game over flag

def check_stair_below_player():
    for stair in stairs:
        if player.rect.colliderect(stair.rect):
            return True
    return False

# Font settings
font = pg.font.SysFont('Arial', 20)
Overfont = pg.font.SysFont('Arial', 40)

# Start the Loop of game
done = False
clock = pg.time.Clock()
game_started = False  # Game start flag
game_over = False  # Game over flag

while not done:
    clock.tick(30)

    # Handle event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if game_over:
                    init_game()
                else:
                    player.change_direction()
            elif event.key == pg.K_LSHIFT and not game_over:
                if not game_started:
                    game_started = True
                    start_ticks = pg.time.get_ticks()  # Start timer
                player.move()
                if not check_stair_below_player():  # Check if there is a stair below the player
                    game_over = True  # Set game over flag
                    game_started = False  # Stop the game
                    if score > high_score:
                        high_score = score
                    score = 0
                    pg.time.delay(500)
                else:
                    add_new_stair()
                    for stair in stairs:
                        stair.update()
                    score += 1
                    if score % 5 == 0 and time_limit > 0.5:
                        time_limit *= 0.8
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
            game_over = True  # Set game over flag
            game_started = False  # Stop the game
            if score > high_score:
                high_score = score
            score = 0
    else:
        seconds = time_limit  # Display full time limit if game hasn't started

    # Clear screen
    screen.fill(WHITE)

    all_sprites.draw(screen)

    # Draw BLUE rectangles for score and controls text backgrounds
    pg.draw.rect(screen, BLACK, (0, height - 60, width, 60))
    pg.draw.rect(screen, BLUE, ( 5, height - 55, width - 10, 50))
    pg.draw.rect(screen, BLACK, (0, 0, width, 60))

    # Render score and timer
    score_text = font.render(f'Score: {score}', True, WHITE)
    high_score_text = font.render(f'High Score: {high_score}', True, WHITE)
    
    controls_text1 = font.render('space_bar : change direction', True, WHITE)
    controls_text2 = font.render('left_shift : move', True, WHITE)

    screen.blit(score_text, (10, height - 60))
    screen.blit(high_score_text, (10, height - 30))
    
    screen.blit(controls_text1, (width - controls_text1.get_width() - 10, height - 60))
    screen.blit(controls_text2, (width - controls_text2.get_width() - 10, height - 30))

    # Render progress bar for timer at the top
    progress_bar_width = width - 10
    progress_bar_height = 50
    progress = seconds / time_limit
    pg.draw.rect(screen, RED, ( 5, 5, progress_bar_width, progress_bar_height))
    pg.draw.rect(screen, GREEN, ( 5, 5, int(progress_bar_width * progress), progress_bar_height))

    # Render game over text
    if game_over:
        screen.fill(WHITE)
        game_over_text1 = Overfont.render('Game Over', True, RED)
        game_over_text2 = font.render('Press space bar', True, RED)
        screen.blit(game_over_text1, (width // 2 - game_over_text1.get_width() // 2, height // 2 - 30))
        screen.blit(game_over_text2, (width // 2 - game_over_text2.get_width() // 2, height // 2 + 50))

    pg.display.flip()

pg.quit()
