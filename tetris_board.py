import pygame

class TetrisBoard:
    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.board = [[0] * width for _ in range(height)]

    def draw_board(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                color = self.board[row][col]
                pygame.draw.rect(screen, color, [col * self.block_size, row * self.block_size, self.block_size, self.block_size])
                pygame.draw.rect(screen, (0, 0, 0), [col * self.block_size, row * self.block_size, self.block_size, self.block_size], 1)

    def update_board(self, piece):
        for row in range(piece.shape_height()):
            for col in range(piece.shape_width()):
                if piece.shape[row][col]:
                    self.board[piece.y + row][piece.x + col] = piece.color

    def is_collision(self, piece):
        for row in range(piece.shape_height()):
            for col in range(piece.shape_width()):
                if piece.shape[row][col] and self.board[piece.y + row][piece.x + col]:
                    return True
        return False
