import pygame

WIDTH, HEIGHT = 800, 800  # pixel size
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# player colors
RED = (255, 0, 0)  # (palette RGB)
GREEN = (124, 252, 0)

# filed colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0,0,255)

CROWN = pygame.transform.scale(pygame.image.load("./checkers/assets/crown.png"), (40,25)) # "/" == "\\"
