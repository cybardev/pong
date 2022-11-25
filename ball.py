import pygame
from values import *
from random import choice


class Ball(pygame.sprite.Sprite):
    """Class to represent a ball in the game"""

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the ball, its width and height
        # Set the background color to transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball
        pygame.draw.rect(self.image, color, [X, Y, width, height])

        # Set initial velocity
        self.velocity = [choice((-BALL_VELOCITY, BALL_VELOCITY)), BALL_VELOCITY]

        # Fetch the rectangle object that has the dimensions of the image
        self.rect: pygame.rect.Rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[X]
        self.rect.y += self.velocity[Y]
