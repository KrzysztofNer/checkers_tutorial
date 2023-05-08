import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, GREEN, RED
from checkers.game import Game
from checkers.board import Board

FPS = 60

screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")  # create the name of display caption


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(screen)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if user clicked "close display"
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if game.turn == GREEN:
                    game.select(row, col)
                elif game.turn == RED:
                    game.select(row, col)

        game.update()

    pygame.quit()

main()
