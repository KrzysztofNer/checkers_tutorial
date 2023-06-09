import pygame
from .constants import RED, GREEN, BLUE, SQUARE_SIZE
from .board import Board


class Game:
    def __init__(self, win):
        self._initialization()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _initialization(self):
        self.selected_piece = None
        self.board = Board()
        self.turn = GREEN
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._initialization()

    def select(self, row, col) -> bool:
        if self.selected_piece:
            result = self._move(row, col)
            if not result:
                self.selected_piece = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)  # piece = object with row, col and color

        if piece != 0 and piece.color == self.turn:
            self.selected_piece = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected_piece and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected_piece, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,
                               (SQUARE_SIZE * col + SQUARE_SIZE // 2, SQUARE_SIZE * row + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == GREEN:
            self.turn = RED
        else:
            self.turn = GREEN

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()