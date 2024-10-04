# imports for pygame project
import pygame
import sys
import button

pygame.init()
pygame.mixer.init()

# creating the display window
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")


main = pygame.image.load('mainmenu.png')  # loading the main menu background
scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
current_background = scaled_main

# sound effects
sound_coins = pygame.mixer.Sound("mixkit-winning-a-coin-video-game-2069.wav")
sound_completion = pygame.mixer.Sound("mixkit-completion-of-a-level-2063.wav")
sound_buttons = pygame.mixer.Sound("mixkit-retro-arcade-casino-notification-211.wav")
sound_bonus = pygame.mixer.Sound("mixkit-extra-bonus-in-a-video-game-2045.wav")
sound_countdown = pygame.mixer.Sound("mixkit-start-countdown-927.wav")
sound_shoot = pygame.mixer.Sound("mixkit-short-laser-gun-shot-1670.wav")
sound_kill = pygame.mixer.Sound("mixkit-unlock-new-item-game-notification-254.wav")

# loading title of game
title_image = pygame.image.load('pixelpaths.png').convert_alpha()
# constructing title
title_button = button.Button(640, 85, title_image, 0.4)

# loading play button
play_image = pygame.image.load('play.png').convert_alpha()
# constructing play button
play_button = button.Button(640, 340, play_image, 0.41)

# loading controls button
controls_image = pygame.image.load('controls.png').convert_alpha()
# constructing controls button
controls_button = button.Button(640, 400, controls_image, 0.41)

# loading custom button
custom_image = pygame.image.load('custom.png').convert_alpha()
# constructing custom button
custom_button = button.Button(640, 480, custom_image, 0.41)

# loading quit button
quit_image = pygame.image.load('quit.png').convert_alpha()
# constructing custom button
quit_button = button.Button(127, 600, quit_image, 0.5)

# loading back button
back_image = pygame.image.load('back.png').convert_alpha()
# constructing back button
back_button = button.Button(55, 26, back_image, 0.9)

# loading keys
keys_image = pygame.image.load('keys.png').convert_alpha()
# constructing keys
keys_button = button.Button(550, 460, keys_image, 0.5)

# loading sfx and music text
music_sfx_image = pygame.image.load('sfx_music.png').convert_alpha()
music_sfx_button = button.Button(400, 120, music_sfx_image, 0.9)

# loading level1 button
level1_image = pygame.image.load('level1.png').convert_alpha()
# constructing level1 button
level1_button = button.Button(420, 250, level1_image, 0.5)

# loading level2 button
level2_image = pygame.image.load('level2.png').convert_alpha()
# constructing level2 button
level2_button = button.Button(850, 143, level2_image, 0.5)

# loading level3 button
level3_image = pygame.image.load('level3.png').convert_alpha()
# constructing level3 button
level3_button = button.Button(640, 360, level3_image, 0.5)

# loading red button
red_image = pygame.image.load('red.png').convert_alpha()
# constructing red button
red_button = button.Button(300, 100, red_image, 0.8)

# loading orange button
orange_image = pygame.image.load('orange.png').convert_alpha()
# constructing orange button
orange_button = button.Button(210, 250, orange_image, 0.8)

# loading yellow button
yellow_image = pygame.image.load('yellow.png').convert_alpha()
# constructing yellow button
yellow_button = button.Button(120, 400, yellow_image, 0.8)

# loading green button
green_image = pygame.image.load('green.png').convert_alpha()
# constructing green button
green_button = button.Button(30, 550, green_image, 0.8)

# loading light blue button
lightblue_image = pygame.image.load('lightblue.png').convert_alpha()
# constructing light blue button
lightblue_button = button.Button(1200, 10, lightblue_image, 0.8)

# loading dark blue button
darkblue_image = pygame.image.load('darkblue.png').convert_alpha()
# constructing dark blue button
darkblue_button = button.Button(1110, 160, darkblue_image, 0.8)

# loading purple button
purple_image = pygame.image.load('purple.png').convert_alpha()
# constructing purple button
purple_button = button.Button(1020, 310, purple_image, 0.8)

# loading pink button
pink_image = pygame.image.load('pink.png').convert_alpha()
# constructing pink button
pink_button = button.Button(930, 440, pink_image, 0.8)

# loading red sprite button
redSprite_image = pygame.image.load('redSprite.png').convert_alpha()
# constructing sprite button
redSprite_button = button.Button(640, 100, redSprite_image, 0.8)

# loading orange sprite button
orangeSprite_image = pygame.image.load('orangeSprite.png').convert_alpha()
# constructing sprite button
orangeSprite_button = button.Button(640, 100, orangeSprite_image, 0.8)

# loading yellow sprite button
yellowSprite_image = pygame.image.load('yellowSprite.png').convert_alpha()
# constructing sprite button
yellowSprite_button = button.Button(640, 100, yellowSprite_image, 0.8)

# loading green sprite button
greenSprite_image = pygame.image.load('greenSprite.png').convert_alpha()
# constructing sprite button
greenSprite_button = button.Button(640, 100, greenSprite_image, 0.8)

# loading light blue sprite button
lightblueSprite_image = pygame.image.load('lightblueSprite.png').convert_alpha()
# constructing sprite button
lightblueSprite_button = button.Button(640, 100, lightblueSprite_image, 0.8)

# loading dark blue sprite button
darkblueSprite_image = pygame.image.load('darkblueSprite.png').convert_alpha()
# constructing sprite button
darkblueSprite_button = button.Button(640, 100, darkblueSprite_image, 0.8)

# loading purple sprite button
purpleSprite_image = pygame.image.load('purpleSprite.png').convert_alpha()
# constructing sprite button
purpleSprite_button = button.Button(640, 100, purpleSprite_image, 0.8)

# loading pink sprite button
pinkSprite_image = pygame.image.load('pinkSprite.png').convert_alpha()
# constructing sprite button
pinkSprite_button = button.Button(640, 100, pinkSprite_image, 0.8)

# loading pause button
pause_image = pygame.image.load('pause.png').convert_alpha()
# constructing pause button
pause_button = button.Button(1200, 30, pause_image, 0.6)

# loading exit button
exit_image = pygame.image.load('exit.png').convert_alpha()
# constructing exit button
exit_button = button.Button(900, 500, exit_image, 0.5)

# loading complete button
complete_image = pygame.image.load('complete.png').convert_alpha()
# constructing complete button
complete_button = button.Button(640, 100, complete_image, 0.8)

# loading resume button
resume_image = pygame.image.load('resume.png').convert_alpha()
# constructing resume button
resume_button = button.Button(640, 500, resume_image, 0.7)

# loading retry button
retry_image = pygame.image.load('retry.png').convert_alpha()
# constructing retry button
retry_button = button.Button(380, 500, retry_image, 0.7)

# loading star button
star1_image = pygame.image.load('star.png').convert_alpha()
# constructing star button
star1_button = button.Button(800, 270, star1_image, 0.7)

# loading star button
star2_image = pygame.image.load('star.png').convert_alpha()
# constructing star button
star2_button = button.Button(470, 270, star2_image, 0.7)


# creating the states
MAIN_MENU = "main_menu"
PLAY = "play"
CONTROLS = "controls"
CUSTOM = "custom"
LEVEL1 = "level1"
LEVEL2 = "level2"
LEVEL3 = "level3"
PAUSE1 = "pause1"
PAUSE2 = "pause2"
PAUSE3 = "pause3"
GAME_OVER = "game_over"
COMPLETE1 = "complete1"  # first level
COMPLETE2 = "complete2"  # second level
COMPLETE3 = "complete3"  # third level
BONUS_ROUND = "bonus_round"
BONUS_ROUND2 = "bonus_round2"
SHOOT = "shooting"

state = MAIN_MENU


# setting all sprite visibility to false expect light blue
red_sprite_visible = False
orange_sprite_visible = False
yellow_sprite_visible = False
green_sprite_visible = False
lightblue_sprite_visible = True  # default colour
darkblue_sprite_visible = False
purple_sprite_visible = False
pink_sprite_visible = False

selected_sprite = lightblueSprite_image

# play function
def play():
    global main, current_background,state
    state = PLAY
    pygame.display.set_caption("Levels")
    play_background = pygame.image.load('black.png').convert_alpha() # loading a black image for the background
    current_background = play_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    pygame.display.update()


# controls function
def controls():
    global main, current_background, state
    state = CONTROLS
    pygame.display.set_caption("Controls")
    controls_background = pygame.image.load('black.png').convert_alpha() # loading a black image for the background
    current_background = controls_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    pygame.display.update()

# custom function
def custom():
    global main, current_background, state
    state = CUSTOM
    pygame.display.set_caption("Custom")
    custom_background = pygame.image.load('black.png').convert_alpha() # loading a black image for the background
    current_background = custom_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    pygame.display.update()

# level 1 function
def level1():
    global main, current_background, state, sprite_x, sprite_y, initial_sprite_x, initial_sprite_y
    state = LEVEL1
    pygame.display.set_caption("Level 1")
    custom_background = pygame.image.load('black.png').convert_alpha()  # loading a black image for the background
    current_background = custom_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    sprite_x, sprite_y = initial_sprite_x, initial_sprite_y  # Reset the sprite's position
    pygame.display.update()

# level 2 function
def level2():
    global main, current_background, state, sprite_x, sprite_y, initial_sprite_x, initial_sprite_y
    state = LEVEL2
    pygame.display.set_caption("Level 2")
    custom_background = pygame.image.load('black.png').convert_alpha()  # loading a black image for the background
    current_background = custom_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    sprite_x, sprite_y = initial_sprite_x, initial_sprite_y  # Reset the sprite's position
    pygame.display.update()

# level 2 function
def level3():
    global main, current_background, state, sprite_x, sprite_y, initial_sprite_x, initial_sprite_y
    state = LEVEL3
    pygame.display.set_caption("Level 3")
    custom_background = pygame.image.load('black.png').convert_alpha()  # loading a black image for the background
    current_background = custom_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    sprite_x, sprite_y = initial_sprite_x, initial_sprite_y  # Reset the sprite's position
    pygame.display.update()

# pause function
def pause1():
    global main, current_background, state, scaled_main
    state = PAUSE1
    pygame.display.set_caption("Pause")
    main = pygame.image.load('pausemenu.png')  # loading the main menu background
    scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
    current_background = scaled_main

def pause2():
    global main, current_background, state, scaled_main
    state = PAUSE2
    pygame.display.set_caption("Pause")
    main = pygame.image.load('pausemenu.png')  # loading the main menu background
    scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
    current_background = scaled_main

def pause3():
    global main, current_background, state, scaled_main
    state = PAUSE3
    pygame.display.set_caption("Pause")
    main = pygame.image.load('pausemenu.png')  # loading the main menu background
    scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
    current_background = scaled_main

def complete1():
    global main, current_background, state
    state = COMPLETE1
    pygame.display.set_caption("Level 1 Complete")
    custom_background = pygame.image.load('black.png').convert_alpha()  # loading a black image for the background
    current_background = custom_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    pygame.display.update()

def complete2():
    global main, current_background, state
    state = COMPLETE2
    pygame.display.set_caption("Level 2 Complete")
    custom_background = pygame.image.load('black.png').convert_alpha()  # loading a black image for the background
    current_background = custom_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    pygame.display.update()

def complete3():
    global main, current_background, state
    state = COMPLETE3
    pygame.display.set_caption("Level 3 Complete")
    custom_background = pygame.image.load('black.png').convert_alpha()  # loading a black image for the background
    current_background = custom_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    pygame.display.update()


# function for bonus round

clock = pygame.time.Clock()
start = 1000
start2 = 1000
def bonus_round():
    global main, current_background, state, sprite_x, sprite_y
    state = BONUS_ROUND
    pygame.display.set_caption("Bonus Round")
    custom_background = pygame.image.load('black.png').convert_alpha()  # loading a black image for the background
    current_background = custom_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    sprite_x, sprite_y = 10 * TILESIZE, 10 * TILESIZE
    pygame.display.update()

def bonus_round2():
    global main, current_background, state, sprite_x, sprite_y
    state = BONUS_ROUND2
    pygame.display.set_caption("Bonus Round")
    custom_background = pygame.image.load('black.png').convert_alpha()  # loading a black image for the background
    current_background = custom_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    sprite_x, sprite_y = 11 * TILESIZE, 10 * TILESIZE
    pygame.display.update()


# SPRITES AND SPRITE MOVEMENT


GREEN = (128, 255, 0)  # temporary
BLACK = (0, 0, 0)

TILESIZE = 60  # initialising tile size
grid_width = screen_width / TILESIZE
grid_height = screen_height / TILESIZE
# wall positions, array for coordinates
level1_walls = [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11),
                (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11),
                (11, 11), (12, 11), (13, 11), (14, 11), (15, 11), (16, 11), (17, 11), (18, 11), (19, 11),
                (20, 11), (21, 11),
                (21, 2), (21, 3), (21, 4), (21, 5), (21, 6), (21, 7), (21, 8), (21, 9), (21, 10), (21, 11),
                (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (8, 9), (8, 8), (8, 10), (8, 7), (7, 7),
                (9, 7), (10, 7), (11, 7), (6, 7), (5, 7), (4, 7),
                (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2),
                (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (18, 2), (19, 2), (20, 2),
                (1, 5), (2, 5), (6, 5), (6, 4), (6, 6), (8, 3), (8, 4),
                (16, 3), (18, 3), (16, 4), (18, 4),(16, 5), (18, 5), (16, 6), (15, 6), (10, 5), (11, 5), (12, 5),
                (13, 5), (16, 7), (17, 7), (18, 7), (13, 7), (13, 8), (13, 9), (16, 8), (16, 9)
                ]
# level 2 wall positions
level2_walls = [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11),
                (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11),
                (11, 11), (12, 11), (13, 11), (14, 11), (15, 11), (16, 11), (17, 11), (18, 11), (19, 11),
                (20, 11), (21, 11),
                (21, 2), (21, 3), (21, 4), (21, 5), (21, 6), (21, 7), (21, 8), (21, 9), (21, 10), (21, 11),
                (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2),
                (11, 2), (17, 2), (13, 2), (14, 2), (15, 2), (16, 2), (18, 2), (19, 2), (20, 2),
                (2, 10), (2, 9), (2, 8), (2, 7), (4, 9), (5, 9), (6, 9), (6, 10), (1, 5), (2, 5), (3, 7), (4, 7),
                (2, 4), (4, 6), (4, 5), (4, 4), (4, 9), (6, 3), (5, 5), (6, 5), (7, 5), (9, 3), (9, 4), (9, 5), (9, 6),
                (6, 7), (7, 7), (8, 7), (9, 7), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9), (12, 10), (11, 7), (11, 6),
                (11, 5), (11, 4), (10, 4), (12, 7), (13, 7), (14, 7), (14, 8), (14, 9), (15, 9), (17, 10), (17, 9),
                (17, 8), (17, 6), (18, 6), (19, 6), (19, 7), (19, 9), (14, 6), (15, 6), (16, 6), (19, 6), (20, 4), (18, 4),
                (18, 5), (16, 3), (16, 4), (15, 4), (14, 4), (13, 4)
               ]
level3_walls = [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11),
                (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11),
                (11, 11), (12, 11), (13, 11), (14, 11), (15, 11), (16, 11), (17, 11), (18, 11), (19, 11),
                (20, 11), (21, 11),(2, 4),
                (21, 2), (21, 3), (21, 4), (21, 5), (21, 6), (21, 7), (21, 8), (21, 9), (21, 10), (21, 11),
                (9, 9), (3, 10), (4, 9), (2, 8), (5, 8), (3, 7), (4, 6), (3, 6), (6, 8), (7, 8), (9, 10), (6, 6),
                (7, 6), (8, 6), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2),
                (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (19, 2), (20, 2),
                (9, 8), (10, 7), (11, 6), (7, 3), (7, 4), (9, 5), (9, 4), (9, 3), (1, 4), (2, 5), (7, 9), (7, 10),
                (10, 4), (11, 4), (12, 4), (13, 4), (13, 5), (13, 6), (13, 7), (14, 7), (15, 7), (16, 7), (17, 7),
                (19, 7), (19, 9), (19, 5), (18, 4), (18, 8), (19, 3), (17, 5), (16, 5), (15, 5), (16, 3)
               ]

# initialising the starting position
initial_sprite_x, initial_sprite_y = 1 * TILESIZE, 10 * TILESIZE
# sprite starting coordinates
sprite_x, sprite_y = initial_sprite_x, initial_sprite_y

score1 = 0  # starting score for level 1
score2 = 0  # starting score for level 2
score3 = 0  # starting score for level 3


# function for drawing out the grid lines
def draw_grid():
    for x in range(0, screen_width, TILESIZE):
        pygame.draw.line(screen, GREEN, (x, 0), (x, screen_height))
    for y in range(0, screen_height, TILESIZE):
        pygame.draw.line(screen, GREEN, (0, y), (screen_width, y))

# displaying sprite
def display_sprite(tile_x, tile_y):
    global selected_sprite, TILESIZE, sprite_image
    # loading sprite on grid
    if selected_sprite == redSprite_image:
        sprite_image = pygame.image.load('redSprite.png').convert_alpha()
    elif selected_sprite == orangeSprite_image:
        sprite_image = pygame.image.load('orangeSprite.png').convert_alpha()
    elif selected_sprite == yellowSprite_image:
        sprite_image = pygame.image.load('yellowSprite.png').convert_alpha()
    elif selected_sprite == greenSprite_image:
        sprite_image = pygame.image.load('greenSprite.png').convert_alpha()
    elif selected_sprite == lightblueSprite_image:
        sprite_image = pygame.image.load('lightblueSprite.png').convert_alpha()
    elif selected_sprite == darkblueSprite_image:
        sprite_image = pygame.image.load('darkblueSprite.png').convert_alpha()
    elif selected_sprite == purpleSprite_image:
        sprite_image = pygame.image.load('purpleSprite.png').convert_alpha()
    elif selected_sprite == pinkSprite_image:
        sprite_image = pygame.image.load('pinkSprite.png').convert_alpha()
    sprite_image = pygame.transform.scale(sprite_image, (TILESIZE, TILESIZE))  # scale it to fit a grid box
    screen_pos = tile_x * TILESIZE, tile_y * TILESIZE
    screen.blit(sprite_image, screen_pos)
    return sprite_image

# function for drawing walls on the map - level 1
def draw_walls_1():
    global TILESIZE, level1_walls
    wall_colour = (128, 0, 178)  # purple walls
    for pos in level1_walls:
        wall_x = pos[0] * TILESIZE
        wall_y = pos[1] * TILESIZE
        pygame.draw.rect(screen, wall_colour, (wall_x, wall_y, TILESIZE, TILESIZE))

# function for drawing walls in level 2
def draw_walls_2():
    global TILESIZE, level2_walls
    wall_colour = (128, 0, 178)  # purple walls
    for pos in level2_walls:
        wall_x = pos[0] * TILESIZE
        wall_y = pos[1] * TILESIZE
        pygame.draw.rect(screen, wall_colour, (wall_x, wall_y, TILESIZE, TILESIZE))

# level 3 walls
def draw_walls_3():
    global TILESIZE, level3_walls
    wall_colour = (128, 0, 178)  # purple walls
    for pos in level3_walls:
        wall_x = pos[0] * TILESIZE
        wall_y = pos[1] * TILESIZE
        pygame.draw.rect(screen, wall_colour, (wall_x, wall_y, TILESIZE, TILESIZE))


# scoring
def draw_score1(score1):
    font = pygame.font.SysFont('Emulogic', 50, bold=True)
    score1_text = font.render(f"S C O R E : {score1}", True, (255, 255, 255))  # Render the score in white color
    screen.blit(score1_text, (10, 75))  # output score top-left corner

def draw_score2(score2):
    font = pygame.font.SysFont('Emulogic', 50, bold=True)
    score2_text = font.render(f"S C O R E : {score2}", True, (255, 255, 255))  # Render the score in white color
    screen.blit(score2_text, (10, 75))  # output score top-left corner

def draw_score3(score3):
    font = pygame.font.SysFont('Emulogic', 50, bold=True)
    score3_text = font.render(f"S C O R E : {score3}", True, (255, 255, 255))  # Render the score in white color
    screen.blit(score3_text, (10, 75))  # output score top-left corner


# coins
coin_image = pygame.image.load('coin.png').convert_alpha()  # loading coin image
coin_image = pygame.transform.scale(coin_image, (35, 35))  # scale to fit the grid
# coin placement
level1_coins = [(7, 10), (7, 9), (7, 8), (1, 3), (1, 4), (2, 3), (2, 4), (5, 3), (5, 4), (5, 5), (5, 6), (6, 3), (7, 3),
                (7, 4), (7, 5), (7, 6), (10, 4), (11, 4), (12, 4), (13, 4), (9, 10), (9, 9), (9, 8),
                (17, 3), (17, 4), (17, 5), (19, 3), (19, 4), (19, 5), (20, 3), (20, 4), (20, 5), (15, 10), (16, 10),
                (17, 10), (18, 10), (1, 6), (1, 7), (1, 8),(15, 10), (15, 10), (10, 3), (11, 3), (12, 3), (13, 3)
                ]
level2_coins = [(1, 9), (1, 8), (1, 7), (1, 6), (1, 4), (1, 3), (2, 3), (8, 3), (8, 4), (8, 5), (8, 6), (8, 10),
                (9, 10), (10, 10), (11, 10), (15, 8), (15, 7), (20, 10), (20, 9), (20, 8), (19, 10), (19, 8), (18, 10),
                (18, 9), (18, 8), (20, 3), (19, 3), (19, 4), (19, 5), (20, 5), (12, 3), (12, 4), (12, 5), (12, 6),
                (13, 6), (18, 9), (20, 6),(20, 7), (10, 5), (10, 6), (10, 7)]
bonus_coins = [(15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (16, 3), (16, 4), (16, 5), (16, 6), (16, 7),
               (16, 8), (16, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2),
               (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8),
               (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8),
               (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8),
               (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7),
               (12, 8), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (14, 3), (14, 4), (14, 5), (14, 6),
               (14, 7), (14, 8), (16, 2), (16, 3), (16, 4), (16, 5), (16, 6), (16, 7), (16, 8),
               (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
               (17, 3), (17, 4), (17, 5), (17, 6), (17, 7), (17, 8), (17, 2), (3, 2),
               (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9),
               (15, 9), (16, 9), (17, 9)
               ]
bonus_coins2 = [(15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (16, 3), (16, 4), (16, 5), (16, 6), (16, 7),
               (16, 8), (16, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2),
               (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8),
               (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8),
               (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8),
               (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7),
               (12, 8), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (14, 3), (14, 4), (14, 5), (14, 6),
               (14, 7), (14, 8), (16, 2), (16, 3), (16, 4), (16, 5), (16, 6), (16, 7), (16, 8),
               (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
               (17, 3), (17, 4), (17, 5), (17, 6), (17, 7), (17, 8), (17, 2), (3, 2),
               (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9),
               (15, 9), (16, 9), (17, 9)
               ]

level3_coins = [(2, 6), (2, 7), (3, 9), (3, 8), (2, 9), (2, 10), (1, 3), (4, 8), (4, 7), (3, 5), (6, 5), (6, 4),
                (6, 3), (7, 5), (8, 5), (8, 4), (8, 3), (9, 7), (9, 6), (10, 6), (8, 7), (8, 8), (8, 9), (10, 5),(11, 5)
                , (19, 10), (20, 10), (20, 9), (20, 8), (20, 7), (20, 6), (20, 5), (20, 4), (20, 3), (19, 8), (19, 4),
                (19, 6), (18, 6), (18, 5), (18, 7), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (15, 4),
                (16, 4), (17, 3), (17, 4), (4, 5)
                ]

# level1
# function for placing the coins
def draw_coins_1():
    for coin_pos in level1_coins:
        coin_x = coin_pos[0] * TILESIZE + 15
        coin_y = coin_pos[1] * TILESIZE + 15
        screen.blit(coin_image, (coin_x, coin_y))
# coin collisions
def coin_collision1(sprite_x, sprite_y):
    global score1
    sprite_pos = (sprite_x // TILESIZE, sprite_y // TILESIZE)
    if sprite_pos in level1_coins:
        sound_coins.play()
        level1_coins.remove(sprite_pos)
        score1 += 50  # +50 points to the score
# level2
def draw_coins_2():
    for coin_pos in level2_coins:
        coin_x = coin_pos[0] * TILESIZE + 15
        coin_y = coin_pos[1] * TILESIZE + 15
        screen.blit(coin_image, (coin_x, coin_y))
# coin collisions
def coin_collision2(sprite_x, sprite_y):
    global score2
    sprite_pos = (sprite_x // TILESIZE, sprite_y // TILESIZE)
    if sprite_pos in level2_coins:
        sound_coins.play()
        level2_coins.remove(sprite_pos)
        score2 += 50  # +50 points to the score

# bonus round coins
def draw_coins_b():
    for coin_pos in bonus_coins:
        coin_x = coin_pos[0] * TILESIZE + 15
        coin_y = coin_pos[1] * TILESIZE + 15
        screen.blit(coin_image, (coin_x, coin_y))

def coin_collision_b(sprite_x, sprite_y):
    global score2
    sprite_pos = (sprite_x // TILESIZE, sprite_y // TILESIZE)
    if sprite_pos in bonus_coins:
        bonus_coins.remove(sprite_pos)
        score2 += 50  # +50 points to the score

def draw_coins_b2():
    for coin_pos in bonus_coins2:
        coin_x = coin_pos[0] * TILESIZE + 15
        coin_y = coin_pos[1] * TILESIZE + 15
        screen.blit(coin_image, (coin_x, coin_y))

def coin_collision_b2(sprite_x, sprite_y):
    global score3
    sprite_pos = (sprite_x // TILESIZE, sprite_y // TILESIZE)
    if sprite_pos in bonus_coins2:
        bonus_coins2.remove(sprite_pos)
        score3 += 50  # +50 points to the score

def draw_coins_3():
    for coin_pos in level3_coins:
        coin_x = coin_pos[0] * TILESIZE + 15
        coin_y = coin_pos[1] * TILESIZE + 15
        screen.blit(coin_image, (coin_x, coin_y))
# coin collisions
def coin_collision3(sprite_x, sprite_y):
    global score3
    sprite_pos = (sprite_x // TILESIZE, sprite_y // TILESIZE)
    if sprite_pos in level3_coins:
        sound_coins.play()
        level3_coins.remove(sprite_pos)
        score3 += 50  # +50 points to the score


# trophy
trophy_image = pygame.image.load('trophy.png').convert_alpha()  # loading coin image
trophy_image = pygame.transform.scale(trophy_image, (58, 58))  # scale to fit the grid
trophy_position1 = (17, 2)
trophy_position2 = (12, 2)
trophy_position3 = (18, 2)

# level1
# function to draw the trophy on the screen
def draw_trophy1():
    trophy_x = trophy_position1[0] * TILESIZE
    trophy_y = trophy_position1[1] * TILESIZE
    screen.blit(trophy_image, (trophy_x, trophy_y))

# function to check for collision with the trophy
def trophy_collision1(sprite_x, sprite_y):
    global state
    sprite_pos = (sprite_x // TILESIZE, sprite_y // TILESIZE)
    if sprite_pos == trophy_position1:
        sound_completion.play()
        return True
    return False

# level2
def draw_trophy2():
    trophy_x = trophy_position2[0] * TILESIZE
    trophy_y = trophy_position2[1] * TILESIZE
    screen.blit(trophy_image, (trophy_x, trophy_y))

def trophy_collision2(sprite_x, sprite_y):
    global state
    sprite_pos = (sprite_x // TILESIZE, sprite_y // TILESIZE)
    if sprite_pos == trophy_position2:
        sound_completion.play()
        return True
    return False

# level 3
def draw_trophy3():
    trophy_x = trophy_position3[0] * TILESIZE
    trophy_y = trophy_position3[1] * TILESIZE
    screen.blit(trophy_image, (trophy_x, trophy_y))

def trophy_collision3(sprite_x, sprite_y):
    global state
    sprite_pos = (sprite_x // TILESIZE, sprite_y // TILESIZE)
    if sprite_pos == trophy_position3:
        sound_completion.play()
        return True
    return False

# BONUS ROUND


# portal
portal_image = pygame.image.load('portal.png').convert_alpha()  # loading portal image
portal_image = pygame.transform.scale(portal_image, (60, 60))  # scale to fit the grid
portal_position = (5, 10)
portal_position2 = (1, 3)

# drawing portal on screen
portal_draw = True
portal_draw2 = True
def draw_portal():
    if portal_draw:
        portal_x = portal_position[0] * TILESIZE
        portal_y = portal_position[1] * TILESIZE
        screen.blit(portal_image, (portal_x, portal_y))
    return True

# function to check for collision with the portal
def portal_collision(sprite_x, sprite_y):
    global state
    sprite_pos = (sprite_x // TILESIZE, sprite_y // TILESIZE)
    if sprite_pos == portal_position:
        return True
    return False

def draw_portal2():
    if portal_draw2:
        portal_x = portal_position2[0] * TILESIZE
        portal_y = portal_position2[1] * TILESIZE
        screen.blit(portal_image, (portal_x, portal_y))
    return True

# function to check for collision with the portal
def portal_collision2(sprite_x, sprite_y):
    global state
    sprite_pos = (sprite_x // TILESIZE, sprite_y // TILESIZE)
    if sprite_pos == portal_position2:
        return True
    return False


# SHOOTING


# bullets
ammo_image = pygame.image.load('ammo.png').convert_alpha()  # loading bullets image
ammo_image = pygame.transform.scale(ammo_image, (50, 50))  # scale to fit the grid
ammo_position = (8, 10)


# drawing ammo on screen
draw_ammo = True
def draw_bullets():
    if draw_ammo:
        bullets_x = ammo_position[0] * TILESIZE + 5
        bullets_y = ammo_position[1] * TILESIZE
        screen.blit(ammo_image, (bullets_x, bullets_y))
    return True

# function to check for collision with the bullets
def bullets_collision(sprite_x, sprite_y):
    global state
    sprite_pos = (sprite_x // TILESIZE, sprite_y // TILESIZE)
    if sprite_pos == ammo_position:
        return True
    return False


# enemy
enemy_image = pygame.image.load('enemy.png').convert_alpha()  # loading enemy image
enemy_image = pygame.transform.scale(enemy_image, (60, 60))  # scale to fit the grid

enemy_draw = True

move_time = 1500  # 1.5 seconds
last_switch_time = 0  # checks when the enemy pos was last changed
sprite_at_first_position = True
enemy_position_1 = (14, 9)
enemy_position_2 = (15, 9)

def draw_moving_enemy():
    global last_switch_time, sprite_at_first_position
    current_time = pygame.time.get_ticks()
    if current_time - last_switch_time >= move_time: # checks if it's been 1.5s
        sprite_at_first_position = not sprite_at_first_position  # alternates pos
        last_switch_time = current_time
    if sprite_at_first_position:
        current_position = enemy_position_1
    else:
        current_position = enemy_position_2

    enemy_x = current_position[0] * TILESIZE
    enemy_y = current_position[1] * TILESIZE
    screen.blit(enemy_image, (enemy_x, enemy_y))


max_bullets = 5
class Bullets:
    def __init__(self, x, y):
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.spawn_time = pygame.time.get_ticks()
        self.active = True

    def update(self):
        if self.active:
            self.rect.x += 5  # move bullet to the right
            if pygame.time.get_ticks() - self.spawn_time >= 200:
                self.active = False

    def draw(self, surface):
        if self.active:  # Only draw if bullet is active
            surface.blit(self.image, self.rect)  # Draw bullet

    def is_active(self):
        return self.active


    def get_position(self):  # gets pos of bullet
        return (self.rect.x, self.rect.y)


bullets = []
last_shot_time = 0  # to track the last time a bullet was shot
shoot_delay = 250   # time in milliseconds to wait before allowing another bullet

fire_ammo = False

singular_bullet_image = pygame.image.load("singular_bullet.png").convert_alpha()
singular_bullet_image = pygame.transform.scale(singular_bullet_image, (15, 50))  # scale to fit the grid
ammo_position1 = (5 * TILESIZE, 1.1 * TILESIZE)
ammo_position2 = (6 * TILESIZE, 1.1 * TILESIZE)
ammo_position3 = (7 * TILESIZE, 1.1 * TILESIZE)
ammo_position4 = (8 * TILESIZE, 1.1 * TILESIZE)
ammo_position5 = (9 * TILESIZE, 1.1 * TILESIZE)
ammo_tally = [ammo_position1, ammo_position2, ammo_position3, ammo_position4, ammo_position5]


# HEALTH


max_health = 15  # max health
current_health = 15
health_bar_width = 400  # width of the health bar
health_bar_height = 60  # height of the health bar

white = (255, 255, 255)
collided = False

def draw_health_bar():
    health_percentage = current_health / max_health
    current_bar_width = int(health_percentage * health_bar_width)
    # drawing health bar
    pygame.draw.rect(screen, white, (0, 0, health_bar_width, health_bar_height), 8)
    # filling in the health bar amount
    if current_bar_width > 0:
        pygame.draw.rect(screen, GREEN, (4, 4, current_bar_width - 10, health_bar_height - 10))

# initialize the timer for health reduction


last_collision_time = 0
collision_cooldown = 2000  # 5 seconds in milliseconds

# function to check for collision with the enemy
def enemy_collision(sprite_x, sprite_y):
    global current_health, collided, last_collision_time, collision_cooldown
    sprite_pos = (sprite_x // TILESIZE, sprite_y // TILESIZE)
    current_time = pygame.time.get_ticks()
    if sprite_pos == (13, 9):
        if current_time - last_collision_time > collision_cooldown:
            if not collided:
                current_health -= 5
                if current_health < 0:  # prevent health from going below 0
                    current_health = 0
            last_collision_time = current_time
            collided = True
        else:
            collided = False
    return False


# VOLUME SLIDERS


# loading music and setting initial volume
pygame.mixer.music.load("game-music-loop-6-144641.mp3")
pygame.mixer.music.play(-1)  # loops the music
volume = 0.5
volume2 = 0.5
pygame.mixer.music.set_volume(volume)
sound_coins.set_volume(volume2)
sound_completion.set_volume(volume2)
sound_buttons.set_volume(volume2)
sound_bonus.set_volume(volume2)
sound_countdown.set_volume(volume2)
sound_shoot.set_volume(volume2)
sound_kill.set_volume(volume2)

# sliders settings
slider_x = 660  # x pox of slider
slider_y = 140  # y pos of slider
slider_width = 500
slider_height = 30
# knob on slider
thumb_width = 30
thumb_height = 60
thumb_x = slider_x + int(volume * slider_width) - (thumb_width // 2)  # initial knob position

slider_x_sfx = 660  # x pox of 2nd slider
slider_y_sfx = 270  # y pos of 2nd slider
# knob on 2nd slider
thumb_x_sfx = slider_x_sfx + int(volume2 * slider_width) - (thumb_width // 2)  # initial knob position

# colours
ORANGE = (255, 165, 0)
GREY = (200, 200, 200)

# function for drawing slider
def draw_slider():
    # drawing slider
    pygame.draw.rect(screen, GREY, (slider_x, slider_y, slider_width, slider_height))
    # drawing knob
    pygame.draw.rect(screen, ORANGE, (thumb_x, slider_y - (thumb_height // 2) + 10, thumb_width, thumb_height))
    # drawing 2nd slider
    pygame.draw.rect(screen, GREY, (slider_x_sfx, slider_y_sfx, slider_width, slider_height))
    # 2nd knob
    pygame.draw.rect(screen, ORANGE, (thumb_x_sfx, slider_y_sfx - (thumb_height // 2) + 10, thumb_width, thumb_height))


drag1 = False
drag2 = False


# running the game loop
run = True
while run:
    key_handled = False
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # once right mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (thumb_x <= mouse_x <= thumb_x + thumb_width and
                    slider_y - (thumb_height // 2) <= mouse_y <= slider_y + (thumb_height // 2)):
                drag1 = True
        # letting go of right mouse
        if event.type == pygame.MOUSEBUTTONUP:
            drag1 = False

            # Handle mouse motion event
        if event.type == pygame.MOUSEMOTION:
            if drag1:
                mouse_x, _ = pygame.mouse.get_pos()
                # thumb x pos within width range
                thumb_x = max(slider_x - (thumb_width // 2), min(mouse_x, slider_x + slider_width - (thumb_width // 2)))
                # calculate new volume based on the thumb position
                volume = (thumb_x - slider_x + (thumb_width // 2)) / slider_width
                pygame.mixer.music.set_volume(volume)

        # 2nd slider
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x_sfx, mouse_y_sfx = pygame.mouse.get_pos()
            if (thumb_x_sfx <= mouse_x_sfx <= thumb_x_sfx + thumb_width and
                    slider_y_sfx - (thumb_height // 2) <= mouse_y_sfx <= slider_y_sfx + (thumb_height // 2)):
                drag2 = True

        if event.type == pygame.MOUSEBUTTONUP:
            drag2 = False

        if event.type == pygame.MOUSEMOTION:
            if drag2:
                mouse_x_sfx, _ = pygame.mouse.get_pos()
                thumb_x_sfx = max(slider_x_sfx - (thumb_width // 2), min(mouse_x_sfx, slider_x_sfx + slider_width
                                                                         - (thumb_width // 2)))
                volume2 = (thumb_x_sfx - slider_x_sfx + (thumb_width // 2)) / slider_width
                sound_coins.set_volume(volume2)
                sound_completion.set_volume(volume2)
                sound_buttons.set_volume(volume2)
                sound_bonus.set_volume(volume2)
                sound_countdown.set_volume(volume2)
                sound_shoot.set_volume(volume2)
                sound_kill.set_volume(volume2)
        if drag1:
            drag2 = False

    # Handling movement
    keys = pygame.key.get_pressed()
    # Handling movement with collision detection
    new_x, new_y = sprite_x, sprite_y

    if keys[pygame.K_LEFT]:
        new_x -= 1
    if keys[pygame.K_RIGHT]:
        new_x += 1
    if keys[pygame.K_UP]:
        new_y -= 1
    if keys[pygame.K_DOWN]:
        new_y += 1

    # Check for collision with walls
    if state == LEVEL1:
        if (new_x // TILESIZE, new_y // TILESIZE) not in level1_walls:
            sprite_x, sprite_y = new_x, new_y

    if state == LEVEL2:
        if (new_x // TILESIZE, new_y // TILESIZE) not in level2_walls:
            sprite_x, sprite_y = new_x, new_y

    if state == LEVEL3:
        if ((new_x // TILESIZE, new_y // TILESIZE) not in level3_walls and
                (new_x // TILESIZE, new_y // TILESIZE) != enemy_position_1 and enemy_position_2):
            sprite_x, sprite_y = new_x, new_y

    if state == BONUS_ROUND:
        sprite_x, sprite_y = new_x, new_y
    if state == BONUS_ROUND2:
        sprite_x, sprite_y = new_x, new_y

    if fire_ammo:
        if keys[pygame.K_SPACE]:
            # check if enough time has passed since the last shot
            if current_time - last_shot_time > shoot_delay:
                if len(bullets) < max_bullets:
                    bullet = Bullets(sprite_x, sprite_y + 20)
                    bullets.append(bullet)
                    sound_shoot.play()
                    last_shot_time = current_time  # Update the last shot time
                    if ammo_tally:  # only remove if there's ammo left
                        ammo_tally.pop()  # remove one bullet from the tally
                    if not bullet.active:  # monitoring when the bullet is active
                        bullets.remove(bullet)
                    if len(bullets) == 3:
                        enemy_draw = False
                        sound_kill.play()
                        score3 += 50


            pygame.display.flip()  # Update the display

    screen.blit(current_background, (0, 0))  # scaling main menu image

    if state == MAIN_MENU:

        title_button.draw(screen)

        # drawing buttons
        if play_button.draw(screen):
            sound_buttons.play()
            play()

        if controls_button.draw(screen):
            sound_buttons.play()
            controls()

        if custom_button.draw(screen):
            sound_buttons.play()
            custom()

        if quit_button.draw(screen):
            run = False

    elif state == PLAY:
        font = pygame.font.SysFont('Emulogic', 30, bold=True)
        score1_text = font.render(f"S C O R E : {score1}", True, (255, 255, 255))
        score2_text = font.render(f"S C O R E : {score2}", True, (255, 255, 255))
        score3_text = font.render(f"S C O R E : {score3}", True, (255, 255, 255))
        screen.blit(score1_text, (250, 350))  # output score under level1
        screen.blit(score2_text, (680, 350))  # output score under level2
        screen.blit(score3_text, (480, 680))  # output score under level3

        if level1_button.draw(screen):
            sound_buttons.play()
            level1()

        if level2_button.draw(screen):
            sound_buttons.play()
            level2()

        if level3_button.draw(screen):
            sound_buttons.play()
            level3()

        if back_button.draw(screen):  # drawing back button
            sound_buttons.play()
            current_background = scaled_main  # resetting to main menu background
            state = MAIN_MENU
            pygame.display.set_caption("Main Menu")

    elif state == CONTROLS:
        keys_button.draw(screen)  # drawing back button
        if back_button.draw(screen):  # drawing back button
            sound_buttons.play()
            current_background = scaled_main  # resetting to main menu background
            state = MAIN_MENU
            pygame.display.set_caption("Main Menu")
        draw_slider()
        music_sfx_button.draw(screen)

    elif state == CUSTOM:
        # drawing colours out
        if red_button.draw(screen):
            red_sprite_visible = True
            orange_sprite_visible = False
            yellow_sprite_visible = False
            green_sprite_visible = False
            lightblue_sprite_visible = False
            darkblue_sprite_visible = False
            purple_sprite_visible = False
            pink_sprite_visible = False
            selected_sprite = redSprite_image  # updating selected sprite

        if red_sprite_visible:
            redSprite_button.draw(screen)

        if orange_button.draw(screen):
            orange_sprite_visible = True
            red_sprite_visible = False
            yellow_sprite_visible = False
            green_sprite_visible = False
            lightblue_sprite_visible = False
            darkblue_sprite_visible = False
            purple_sprite_visible = False
            pink_sprite_visible = False
            selected_sprite = orangeSprite_image  # updating selected sprite

        if orange_sprite_visible:
            orangeSprite_button.draw(screen)

        if yellow_button.draw(screen):
            yellow_sprite_visible = True
            red_sprite_visible = False
            orange_sprite_visible = False
            green_sprite_visible = False
            lightblue_sprite_visible = False
            darkblue_sprite_visible = False
            purple_sprite_visible = False
            pink_sprite_visible = False
            selected_sprite = yellowSprite_image # updating selected sprite

        if yellow_sprite_visible:
            yellowSprite_button.draw(screen)

        if green_button.draw(screen):
            green_sprite_visible = True
            red_sprite_visible = False
            orange_sprite_visible = False
            yellow_sprite_visible = False
            lightblue_sprite_visible = False
            darkblue_sprite_visible = False
            purple_sprite_visible = False
            pink_sprite_visible = False
            selected_sprite = greenSprite_image  # updating selected sprite

        if green_sprite_visible:
            greenSprite_button.draw(screen)

        if lightblue_button.draw(screen):
            lightblue_sprite_visible = True
            red_sprite_visible = False
            orange_sprite_visible = False
            yellow_sprite_visible = False
            green_sprite_visible = False
            darkblue_sprite_visible = False
            purple_sprite_visible = False
            pink_sprite_visible = False
            selected_sprite = lightblueSprite_image  # updating selected sprite

        if lightblue_sprite_visible:
            lightblueSprite_button.draw(screen)

        if darkblue_button.draw(screen):
            darkblue_sprite_visible = True
            red_sprite_visible = False
            orange_sprite_visible = False
            yellow_sprite_visible = False
            green_sprite_visible = False
            lightblue_sprite_visible = False
            purple_sprite_visible = False
            pink_sprite_visible = False
            selected_sprite = darkblueSprite_image # updating selected sprite

        if darkblue_sprite_visible:
            darkblueSprite_button.draw(screen)

        if purple_button.draw(screen):
            purple_sprite_visible = True
            red_sprite_visible = False
            orange_sprite_visible = False
            yellow_sprite_visible = False
            green_sprite_visible = False
            lightblue_sprite_visible = False
            darkblue_sprite_visible = False
            pink_sprite_visible = False
            selected_sprite = purpleSprite_image  # updating selected sprite

        if purple_sprite_visible:
            purpleSprite_button.draw(screen)

        if pink_button.draw(screen):
            pink_sprite_visible = True
            red_sprite_visible = False
            orange_sprite_visible = False
            yellow_sprite_visible = False
            green_sprite_visible = False
            lightblue_sprite_visible = False
            darkblue_sprite_visible = False
            purple_sprite_visible = False
            selected_sprite = pinkSprite_image  # updating selected sprite

        if pink_sprite_visible:
            pinkSprite_button.draw(screen)

        if back_button.draw(screen):  # drawing back button
            sound_buttons.play()
            current_background = scaled_main  # resetting to main menu background
            state = MAIN_MENU
            pygame.display.set_caption("Main Menu")

    elif state == LEVEL1:
        # loading sprite on grid
        display_sprite(sprite_x // TILESIZE, sprite_y // TILESIZE)
        draw_walls_1()
        draw_score1(score1)
        draw_coins_1()
        coin_collision1(sprite_x, sprite_y)
        draw_trophy1()
        if trophy_collision1(sprite_x, sprite_y):
            complete1()
        if pause_button.draw(screen):
            pause1()

    elif state == LEVEL2:
        # loading sprite on grid
        display_sprite(sprite_x // TILESIZE, sprite_y // TILESIZE)
        draw_score2(score2)
        draw_walls_2()
        draw_coins_2()
        coin_collision2(sprite_x, sprite_y)
        draw_trophy2()
        draw_portal()
        if portal_collision(sprite_x, sprite_y):
            bonus_round()
        if trophy_collision2(sprite_x, sprite_y):
            complete2()
        if pause_button.draw(screen):
            pause2()

    elif state == LEVEL3:
        #draw_grid()
        # loading sprite on grid
        display_sprite(sprite_x // TILESIZE, sprite_y // TILESIZE)
        draw_score3(score3)
        draw_walls_3()
        draw_coins_3()
        coin_collision3(sprite_x, sprite_y)
        draw_trophy3()
        draw_portal2()
        if portal_collision2(sprite_x, sprite_y):
            sound_countdown.play()
            bonus_round2()
        draw_bullets()
        if enemy_draw:
            draw_moving_enemy()  # drawing enemy
        draw_health_bar()
        enemy_collision(sprite_x, sprite_y)
        if bullets_collision(sprite_x, sprite_y):  # once the sprite collides with the ammo on screen
            draw_ammo = False
            fire_ammo = True
        if trophy_collision3(sprite_x, sprite_y):
            complete3()
        if pause_button.draw(screen):
            pause3()
        if fire_ammo:  # once the bullets can be fired
            for position in ammo_tally:
                screen.blit(singular_bullet_image, position)
            for bullet in bullets:
                bullet.update()
            for bullet in bullets:
                bullet.draw(screen)

    elif state == PAUSE1:
        retry_button.draw(screen)
        if exit_button.draw(screen):
            sound_buttons.play()
            main = pygame.image.load('mainmenu.png')  # loading the main menu background
            scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
            current_background = scaled_main
            state = MAIN_MENU
            sprite_x, sprite_y = initial_sprite_x, initial_sprite_y  # Reset sprite position
            pygame.display.set_caption("Main Menu")
        if resume_button.draw(screen):
            sound_buttons.play()
            level1()
            sprite_x, sprite_y = new_x, new_y

    elif state == PAUSE2:
        retry_button.draw(screen)
        if exit_button.draw(screen):
            sound_buttons.play()
            main = pygame.image.load('mainmenu.png')  # loading the main menu background
            scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
            current_background = scaled_main
            state = MAIN_MENU
            sprite_x, sprite_y = initial_sprite_x, initial_sprite_y  # Reset sprite position
            pygame.display.set_caption("Main Menu")
        if resume_button.draw(screen):
            sound_buttons.play()
            level2()
            sprite_x, sprite_y = new_x, new_y

    elif state == PAUSE3:
        retry_button.draw(screen)
        if exit_button.draw(screen):
            sound_buttons.play()
            main = pygame.image.load('mainmenu.png')  # loading the main menu background
            scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
            current_background = scaled_main
            state = MAIN_MENU
            sprite_x, sprite_y = initial_sprite_x, initial_sprite_y  # Reset sprite position
            pygame.display.set_caption("Main Menu")
        if resume_button.draw(screen):
            sound_buttons.play()
            level3()
            sprite_x, sprite_y = new_x, new_y

    elif state == COMPLETE1:
        font = pygame.font.SysFont('Emulogic', 50, bold=True)
        score_text1 = font.render(f"S C O R E : {score1}", True, (255, 255, 255))  # Render the score in white color
        screen.blit(score_text1, (500, 300))  # output score in centre
        star1_button.draw(screen)
        star2_button.draw(screen)
        complete_button.draw(screen)
        if resume_button.draw(screen):
            sound_buttons.play()
            level2()
        retry_button.draw(screen)
        if exit_button.draw(screen):
            sound_buttons.play()
            main = pygame.image.load('mainmenu.png')  # loading the main menu background
            scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
            current_background = scaled_main
            state = MAIN_MENU
            sprite_x, sprite_y = initial_sprite_x, initial_sprite_y  # Reset sprite position
            pygame.display.set_caption("Main Menu")

    elif state == COMPLETE2:
        font = pygame.font.SysFont('Emulogic', 50, bold=True)
        score_text1 = font.render(f"S C O R E : {score2}", True, (255, 255, 255))  # Render the score in white color
        screen.blit(score_text1, (500, 300))  # output score in centre
        star1_button.draw(screen)
        star2_button.draw(screen)
        complete_button.draw(screen)
        if resume_button.draw(screen):
            sound_buttons.play()
            level3()
        retry_button.draw(screen)
        if exit_button.draw(screen):
            sound_buttons.play()
            main = pygame.image.load('mainmenu.png')  # loading the main menu background
            scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
            current_background = scaled_main
            state = MAIN_MENU
            sprite_x, sprite_y = initial_sprite_x, initial_sprite_y  # Reset sprite position
            pygame.display.set_caption("Main Menu")

    elif state == COMPLETE3:
        font = pygame.font.SysFont('Emulogic', 50, bold=True)
        score_text3 = font.render(f"S C O R E : {score3}", True, (255, 255, 255))  # Render the score in white color
        screen.blit(score_text3, (500, 300))  # output score in centre
        star1_button.draw(screen)
        star2_button.draw(screen)
        complete_button.draw(screen)
        retry_button.draw(screen)
        if exit_button.draw(screen):
            sound_buttons.play()
            main = pygame.image.load('mainmenu.png')  # loading the main menu background
            scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
            current_background = scaled_main
            state = MAIN_MENU
            sprite_x, sprite_y = initial_sprite_x, initial_sprite_y  # Reset sprite position
            pygame.display.set_caption("Main Menu")

    elif state == BONUS_ROUND:
        display_sprite(sprite_x // TILESIZE, sprite_y // TILESIZE)
        portal_draw = False
        sound_countdown.play()
        draw_coins_b()
        coin_collision_b(sprite_x, sprite_y)
        start -= 0.35
        if start <= 0:
            sound_bonus.play()
            sprite_x, sprite_y = 4 * TILESIZE, 10 * TILESIZE
            state = LEVEL2
        font = pygame.font.SysFont('Emulogic', 50, bold=True)
        time = font.render(f"T I M E R : {int(start/100)} !", True, (255, 0, 0))  # Render the score in white color
        screen.blit(time, (10, 75))  # output score top-left corner
        score2_text = font.render(f"S C O R E : {score2}", True, (255, 255, 255))  # Render the score in white color
        screen.blit(score2_text, (1000, 75))  # output score top-left corner

    elif state == BONUS_ROUND2:
        portal_draw2 = False
        display_sprite(sprite_x // TILESIZE, sprite_y // TILESIZE)
        draw_coins_b2()
        coin_collision_b2(sprite_x, sprite_y)
        start2 -= 0.35
        if start2 <= 0:
            sound_bonus.play()
            sprite_x, sprite_y = 2 * TILESIZE, 3 * TILESIZE
            state = LEVEL3
        font = pygame.font.SysFont('Emulogic', 50, bold=True)
        time = font.render(f"T I M E R : {int(start2/100)} !", True, (255, 0, 0))  # Render the score in white color
        screen.blit(time, (10, 75))  # output score top-left corner
        score3_text = font.render(f"S C O R E : {score3}", True, (255, 255, 255))  # Render the score in white color
        screen.blit(score3_text, (1000, 75))  # output score top-left corner


    pygame.display.update()
