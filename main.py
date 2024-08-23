# imports for pygame project
import pygame
import sys
import button
import sprite

pygame.init()

# creating the display window
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")


main = pygame.image.load('mainmenu.png')  # loading the main menu background
scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
current_background = scaled_main

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
level3_button = button.Button(640, 300, level3_image, 0.5)

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
exit_button = button.Button(800, 500, exit_image, 0.5)


# creating the states
MAIN_MENU = "main_menu"
PLAY = "play"
CONTROLS = "controls"
CUSTOM = "custom"
LEVEL1 = "level1"
PAUSE = "pause"
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
    global main, current_background,state
    state = CONTROLS
    pygame.display.set_caption("Controls")
    controls_background = pygame.image.load('black.png').convert_alpha() # loading a black image for the background
    current_background = controls_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    pygame.display.update()

# custom function
def custom():
    global main, current_background,state
    state = CUSTOM
    pygame.display.set_caption("Custom")
    custom_background = pygame.image.load('black.png').convert_alpha() # loading a black image for the background
    current_background = custom_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    pygame.display.update()


# level 1 function
def level1():
    global main, current_background, state
    state = LEVEL1
    pygame.display.set_caption("Level 1")
    custom_background = pygame.image.load('black.png').convert_alpha()  # loading a black image for the background
    current_background = custom_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    pygame.display.update()

# pause function
def pause():
    global main, current_background, state, scaled_main
    state = PAUSE
    pygame.display.set_caption("Pause")
    main = pygame.image.load('pausemenu.png')  # loading the main menu background
    scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
    current_background = scaled_main

# SPRITES AND SPRITE MOVEMENT


GREEN = (128, 255, 0)  # temporary

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
                (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (18, 2), (19, 2), (20, 2)

            ]

# sprite starting coordinates
sprite_x, sprite_y = 1 * TILESIZE, 10 * TILESIZE


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

# function for drawing walls on the map
def draw_walls():
    global TILESIZE, level1_walls
    wall_colour = (128, 0, 178)  # purple walls
    for pos in level1_walls:
        wall_x = pos[0] * TILESIZE
        wall_y = pos[1] * TILESIZE
        pygame.draw.rect(screen, wall_colour, (wall_x, wall_y, TILESIZE, TILESIZE))


# running the game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Handling movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite_x -= 1
    if keys[pygame.K_RIGHT]:
        sprite_x += 1
    if keys[pygame.K_UP]:
        sprite_y -= 1
    if keys[pygame.K_DOWN]:
        sprite_y += 1

    screen.blit(current_background, (0, 0))  # scaling main menu image

    if state == MAIN_MENU:

        title_button.draw(screen)

        # drawing buttons
        if play_button.draw(screen):
            print("play")
            play()

        if controls_button.draw(screen):
            print("controls")
            controls()

        if custom_button.draw(screen):
            print("custom")
            custom()

        if quit_button.draw(screen):
            run = False

    elif state == PLAY:
        if level1_button.draw(screen):
            print("1")
            level1()

        if level2_button.draw(screen):
            print("2")

        if level3_button.draw(screen):
            print("3")

        if back_button.draw(screen):  # drawing back button
            current_background = scaled_main  # resetting to main menu background
            state = MAIN_MENU
            pygame.display.set_caption("Main Menu")

    elif state == CONTROLS:
        keys_button.draw(screen)  # drawing back button
        if back_button.draw(screen):
            current_background = scaled_main  # resetting to main menu background
            state = MAIN_MENU
            pygame.display.set_caption("Main Menu")

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
            current_background = scaled_main  # resetting to main menu background
            state = MAIN_MENU
            pygame.display.set_caption("Main Menu")

    elif state == LEVEL1:
        draw_grid()
        # loading sprite on grid
        display_sprite(sprite_x // TILESIZE, sprite_y // TILESIZE)
        draw_walls()
        if pause_button.draw(screen):
            pause()

    elif state == PAUSE:
        if exit_button.draw(screen):
            main = pygame.image.load('mainmenu.png')  # loading the main menu background
            scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
            current_background = scaled_main
            state = MAIN_MENU
            pygame.display.set_caption("Main Menu")

    pygame.display.update()