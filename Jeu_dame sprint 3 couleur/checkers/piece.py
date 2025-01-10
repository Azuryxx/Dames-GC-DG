import pygame
from .constants import PION_1, PION_2, PION_1_bor, PION_2_bor, SQUARE_SIZE

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False  # Si la pièce est une dame (king)

    def make_king(self):
        self.king = True

    def calc_pos(self, offset_x, offset_y):
        self.x = offset_x + self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = offset_y + self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def draw(self, win):
        radius = SQUARE_SIZE // 4  # Taille plus petite du pion
        border_radius = radius + 3  # Bordure ajustée autour du pion

        if self.color == PION_1:
            color = PION_1
            border_color = PION_1_bor
        else:
            color = PION_2
            border_color = PION_2_bor

        pygame.draw.circle(win, border_color, (self.x, self.y), border_radius)
        pygame.draw.circle(win, color, (self.x, self.y), radius)

        if self.king:
            pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), radius + 5, 3)
