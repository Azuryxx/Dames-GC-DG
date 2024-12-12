import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (190, 190, 190, 255)
WHITE = (160, 32, 240, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (255, 0, 0, 255)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))