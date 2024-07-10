# imports for pygame project
import pygame
import sys
import button


pygame.init()

# creating the display window
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")


main = pygame.image.load('mainmenu.png')  # loading the main menu background
scaled_main = pygame.transform.scale(main, (1280, 720))  # scaling down the image to fit the screen
current_background = scaled_main

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
level1_button = button.Button(640, 95, level1_image, 0.6)

# loading level2 button
level2_image = pygame.image.load('level2.png').convert_alpha()
# constructing level2 button
level2_button = button.Button(640, 185, level2_image, 0.6)

# loading level3 button
level3_image = pygame.image.load('level3.png').convert_alpha()
# constructing level3 button
level3_button = button.Button(640, 300, level3_image, 0.6)


MAIN_MENU = "main_menu"
PLAY = "play"
CONTROLS = "controls"
CUSTOM = "custom"
state = MAIN_MENU

# play function
def play():
    global main, current_background,state
    state = PLAY
    pygame.display.set_caption("Play")
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

#custom function
def custom():
    global main, current_background,state
    state = CUSTOM
    pygame.display.set_caption("Custom")
    custom_background = pygame.image.load('black.png').convert_alpha() # loading a black image for the background
    current_background = custom_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    pygame.display.update()





# running the game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(current_background, (0, 0))  # scaling main menu image

    if state == MAIN_MENU:
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
        if level2_button.draw(screen):
            print("2")
        if level3_button.draw(screen):
            print("3")

        if back_button.draw(screen):
            current_background = scaled_main  # resetting to main menu background
            state = MAIN_MENU
            pygame.display.set_caption("Main Menu")

    elif state == CONTROLS:
        keys_button.draw(screen)
        if back_button.draw(screen):
            current_background = scaled_main  # resetting to main menu background
            state = MAIN_MENU
            pygame.display.set_caption("Main Menu")

    elif state == CUSTOM:
        if back_button.draw(screen):
            current_background = scaled_main  # resetting to main menu background
            state = MAIN_MENU
            pygame.display.set_caption("Main Menu")








    pygame.display.update()