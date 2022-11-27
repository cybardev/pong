#!/usr/bin/env python3

import pygame
from values import *
from paddle import Paddle
from ball import Ball
import tkinter as tk
from tkinter import messagebox


class Pong:
    """
    Class to represent a game of Pong
    """

    def __init__(self):
        """Initialize game objects"""

        self.paddles = [
            Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT),
            Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT),
        ]

        self.paddles[P1].rect.x, self.paddles[P1].rect.y = PADDLE_INIT_POS[P1]
        self.paddles[P2].rect.x, self.paddles[P2].rect.y = PADDLE_INIT_POS[P2]

        self.ball = Ball(WHITE, BALL_SIZE, BALL_SIZE)
        self.ball.rect.x, self.ball.rect.y = BALL_INIT_POS

        self.scores = [INIT_SCORE, INIT_SCORE]

        self.all_sprites_list = pygame.sprite.Group()

        self.all_sprites_list.add(self.paddles[P1])
        self.all_sprites_list.add(self.paddles[P2])
        self.all_sprites_list.add(self.ball)

    def play(self):
        """Play a game of Pong"""

        # initialize game engine and interface
        root = tk.Tk()
        root.withdraw()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("gameover.wav")
        screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Pong")
        clock = pygame.time.Clock()

        keep_playing = True
        while keep_playing:
            for event in pygame.event.get():  # for every user action
                if event.type == pygame.QUIT:  # check if user clicked close
                    keep_playing = False  # exit game loop

            # start game
            keys = pygame.key.get_pressed()

            # move the user-controlled paddle when the arrow keys are pressed
            if keys[pygame.K_q]:
                self.paddles[P1].move_up(PADDLE_VELOCITY)
            if keys[pygame.K_a]:
                self.paddles[P1].move_down(PADDLE_VELOCITY)

            # move the computer-controlled paddle to always get the ball
            self.paddles[P2].set_y_pos(
                self.ball.rect.y + (BALL_SIZE - PADDLE_HEIGHT) / 2
            )

            # update all sprites
            self.all_sprites_list.update()

            # bounce the ball if it collides with any of the paddles
            if pygame.sprite.collide_rect(self.ball, self.paddles[P1]):
                self.ball.velocity[X] = abs(self.ball.velocity[X])
            elif pygame.sprite.collide_rect(self.ball, self.paddles[P2]):
                self.ball.velocity[X] = -abs(self.ball.velocity[X])
            else:
                # check ball bounce against walls
                if self.ball.rect.x >= SCREEN_SIZE[X] - BALL_SIZE:
                    self.scores[P1] += SCORE_UNIT
                    self.ball.velocity[X] = -self.ball.velocity[X]
                if self.ball.rect.x <= X:
                    self.scores[P2] += SCORE_UNIT
                    self.ball.velocity[X] = -self.ball.velocity[X]
                if not self.ball.rect.y in range(SCREEN_SIZE[Y] - BALL_SIZE):
                    self.ball.velocity[Y] = -self.ball.velocity[Y]

            # set screen to black
            screen.fill(BLACK)
            # draw centreline
            pygame.draw.line(screen, WHITE, *NET_DIMENSIONS)

            # draw all sprites
            self.all_sprites_list.draw(screen)

            # display scores
            font = pygame.font.Font(None, 74)
            screen.blit(
                font.render(str(self.scores[P1]), USE_ANTIALIASING, WHITE),
                SCORE_POS[P1],
            )
            screen.blit(
                font.render(str(self.scores[P2]), USE_ANTIALIASING, WHITE),
                SCORE_POS[P2],
            )

            # redraw screen to reflect changes
            pygame.display.flip()
            clock.tick(FPS)

            # stop game if score becomes 5 for either player
            if MAX_SCORE in self.scores:
                pygame.mixer.music.play()
                if messagebox.askyesno("Restart Game", "Play again?"):
                    self.__init__()
                else:
                    keep_playing = False

        # exit engine when game loop ends
        pygame.quit()


if __name__ == "__main__":
    game = Pong()
    game.play()
