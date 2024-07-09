import pygame
import sys

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

run = True

# play function

def play():
    global main, current_background,state
    state = PLAY
    pygame.display.set_caption("Play")
    play_background = pygame.image.load('black.png').convert_alpha() # loading a black image for the background
    current_background = play_background  # setting the new current background
    screen.blit(current_background, (0, 0))
    pygame.display.update()

