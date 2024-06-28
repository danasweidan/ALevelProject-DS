import pygame
import sys

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

run = True

def play():
    global main, current_background
    pygame.display.set_caption("Play")
    play_background = pygame.image.load('black.png')
    current_background = play_background
    screen.blit(current_background, (0, 0))
    pygame.display.update()
    screen.fill(0, 0, 0)
    pygame.display.flip()