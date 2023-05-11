import pygame
from .constants import SQUARE_SIZE, CROWN, ROWS


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color    # or self.color: tuple[int, int, int] = color

        self.king = False  # True for test

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        # zobaczymy??? if (self.row == ROWS and self.direction == 1) or (self.row == 0 and self.direction == -1):
        self.king = True

    def draw(self, win):
        radius = int(SQUARE_SIZE / 2 * 0.6)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius, )
        if self.king == True:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
