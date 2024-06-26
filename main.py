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
play_button = button.Button(640, 380, play_image, 0.5)

# loading controls button
controls_image = pygame.image.load('controls.png').convert_alpha()
# constructing controls button
controls_button = button.Button(640, 410, controls_image, 0.5)

# loading custom button
custom_image = pygame.image.load('custom.png').convert_alpha()
# constructing custom button
custom_button = button.Button(640, 440, custom_image, 0.5)

# loading quit button
quit_image = pygame.image.load('quit.png').convert_alpha()
# constructing custom button
quit_button = button.Button(127, 600, quit_image, 0.5)

MAIN_MENU = "main_menu"
PLAY = "play"
state = MAIN_MENU


# play function
def play():
    global main, current_background,state
    state == PLAY
    pygame.display.set_caption("Play")
    play_background = pygame.image.load('black.png').convert_alpha() # loading a black image for the background
    current_background = play_background  # setting the new current background
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

     if custom_button.draw(screen):
          print("custom")

     if quit_button.draw(screen):
        run = False

    if state == PLAY:
        screen.fill(0,0,0)






    pygame.display.update()