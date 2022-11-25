#!/usr/bin/env python3

# Import the pygame library and initialise the game engine
import pygame
from values import *
from paddle import Paddle
from ball import Ball
import tkinter as tk
from tkinter import messagebox


def init_objects():
    paddles = [
        Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT),
        Paddle(WHITE, PADDLE_WIDTH, PADDLE_HEIGHT),
    ]

    paddles[P1].rect.x = 10
    paddles[P1].rect.y = 200

    paddles[P2].rect.x = 670
    paddles[P2].rect.y = 200

    ball = Ball(WHITE, BALL_SIZE, BALL_SIZE)
    ball.rect.x = 340
    ball.rect.y = 195

    scores = [INIT_SCORE, INIT_SCORE]

    all_sprites_list = pygame.sprite.Group()

    all_sprites_list.add(paddles[P1])
    all_sprites_list.add(paddles[P2])
    all_sprites_list.add(ball)

    return paddles, ball, scores, all_sprites_list


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("gameover.wav")

    # Open a new window
    size = SCREEN_SIZE
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")

    paddles, ball, scores, all_sprites_list = init_objects()

    # The loop will carry on until the user exits the game (e.g. clicks the close button).
    keep_playing = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while keep_playing:

        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                keep_playing = False  # Signal to exit loop

        # Start Game
        keys = pygame.key.get_pressed()

        # Moving the user paddle when the arrow keys are pressed (player 2)
        if keys[pygame.K_q]:
            paddles[P2].move_up(PADDLE_VELOCITY)
        if keys[pygame.K_a]:
            paddles[P2].move_down(PADDLE_VELOCITY)

        # Moving the computer paddle to always get the ball (player 1)
        paddles[P1].set_y_pos(ball.rect.y + (BALL_SIZE - PADDLE_HEIGHT) / 2)

        # --- Game logic should go here
        all_sprites_list.update()

        # Bounce the ball if it collides with any of the paddles
        if pygame.sprite.collide_rect(ball, paddles[P1]):
            ball.velocity[X] = abs(ball.velocity[X])
        elif pygame.sprite.collide_rect(ball, paddles[P2]):
            ball.velocity[X] = -abs(ball.velocity[X])
        else:
            # Check if the ball is bouncing against any of the 4 walls:
            if ball.rect.x >= 680:
                scores[P1] += 1
                ball.velocity[X] = -ball.velocity[X]
            if ball.rect.x <= 0:
                scores[P2] += 1
                ball.velocity[X] = -ball.velocity[X]
            if 0 > ball.rect.y or ball.rect.y > 480:
                ball.velocity[Y] = -ball.velocity[Y]

        # --- Drawing code should go here
        # First, clear the screen to black.
        screen.fill(BLACK)
        # Draw the net
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        # Display scores:
        font = pygame.font.Font(None, 74)
        screen.blit(
            font.render(str(scores[P1]), USE_ANTIALIASING, WHITE), (250, 10)
        )
        screen.blit(
            font.render(str(scores[P2]), USE_ANTIALIASING, WHITE), (420, 10)
        )

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(FPS)

        # Stop game if score becomes 5 for either player
        if 5 in (scores[P1], scores[P2]):
            pygame.mixer.music.play()
            if messagebox.askyesno("Restart Game", "Play again?"):
                paddles, ball, scores, all_sprites_list = init_objects()
            else:
                keep_playing = False

    # Once we have exited the main program loop we can stop the game engine:
    pygame.quit()
