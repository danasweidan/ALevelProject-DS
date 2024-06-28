import pygame
import sys

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))


class Button():
    # creating the button
    def __init__(self, xPos, yPos, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.midtop = (xPos, yPos)
        self.clicked = False

    # drawing button on screen
    def draw(self, screen):

        action = False
        # getting mouse position
        pos = pygame.mouse.get_pos()

        # check if mouse is hovering over button

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

