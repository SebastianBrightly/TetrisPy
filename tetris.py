import pygame
from tetris_board import TetrisBoard
from tetris_shapes import get_random_shape

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Initialize game components
clock = pygame.time.Clock()
board = TetrisBoard(WIDTH, HEIGHT)
current_shape = get_random_shape()

# Game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        current_shape.move_left()
    if keys[pygame.K_RIGHT]:
        current_shape.move_right()
    if keys[pygame.K_DOWN]:
        current_shape.move_down()

    # Update and draw the game board
    screen.fill(BLACK)
    board.draw(screen)
    current_shape.draw(screen)
    pygame.display.flip()

pygame.quit()
