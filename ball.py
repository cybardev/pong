import pygame
from values import X, Y, BLACK, BALL_VELOCITY
from random import choice


class Ball(pygame.sprite.Sprite):
    """
    Class to represent a ball
    """

    def __init__(self, color, width, height):
        super().__init__()

        # set attributes
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw the ball
        pygame.draw.rect(self.image, color, [X, Y, width, height])

        # set initial velocity
        self.velocity = [choice((-BALL_VELOCITY, BALL_VELOCITY)), BALL_VELOCITY]

        # get rectangle object with the dimensions of the image
        self.rect: pygame.rect.Rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[X]
        self.rect.y += self.velocity[Y]
