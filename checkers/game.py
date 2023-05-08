import pygame
from .constants import RED, GREEN, BLUE, SQUARE_SIZE
from .board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected_piece = None
        self.board = Board()
        self.turn = GREEN
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col) -> bool:
        # if pygame.MOUSEBUTTONDOWN:
        # pos = pygame.mouse.get_pos()
        # row, col = get_row_col_from_mouse(pos)
        # piece = self.board.get_piece(row, col)
        # self.selected_piece = self.board.move(piece, row, col)
        if self.selected_piece:
            result = self._move(row, col)
            if not result:
                self.selected_piece = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)  # piece = object with row, col and color
            print(row, col, piece)
            if piece != 0 and piece.color == self.turn:
                self.selected_piece = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                print(self.valid_moves)
                return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected_piece and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected_piece, row, col)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (SQUARE_SIZE*col + SQUARE_SIZE//2, SQUARE_SIZE*row + SQUARE_SIZE//2), 15)

    def change_turn(self):
        if self.turn == GREEN:
            self.turn = RED
        else:
            self.turn = GREEN
