import pygame
import sys


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

LIGHTGREY = (100,100,100)

TILESIZE = 32  # initialising tile size
grid_width = screen_width / TILESIZE
grid_height = screen_height / TILESIZE

class spriteMovement():
    def draw_grid(self):
        for x in range(0, screen_width, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, screen_height))
        for y in range(0, screen_height, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (screen_width, y))


