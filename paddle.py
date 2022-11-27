import pygame
from values import *


class Paddle(pygame.sprite.Sprite):
    """
    Class to represent a paddle
    """

    def __init__(self, color, width, height):
        super().__init__()

        # set attributes
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw the paddle
        pygame.draw.rect(self.image, color, [X, Y, width, height])

        # get rectangle object with the dimensions of the image
        self.rect: pygame.rect.Rect = self.image.get_rect()

    def set_y_pos(self, y):
        self.rect.y = y
        self.__validate_y_pos()

    def move_up(self, pixels):
        self.rect.y -= pixels
        self.__validate_y_pos()

    def move_down(self, pixels):
        self.rect.y += pixels
        self.__validate_y_pos()

    def __validate_y_pos(self):
        # keep within screen bounds
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 400:
            self.rect.y = 400
