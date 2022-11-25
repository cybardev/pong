import pygame
from values import *


class Paddle(pygame.sprite.Sprite):
    """
    This class represents a paddle.
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the Paddle, its width and height
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [X, Y, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
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
        # Check that you are not going too far (off the screen)
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 400:
            self.rect.y = 400
