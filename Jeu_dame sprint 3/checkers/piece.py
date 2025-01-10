import pygame
from .constants import PION_1_bor, PION_2_bor, PION_1, PION_2, CROWN, SQUARE_SIZE


class Piece:
    PADDING = 15  # Padding autour du cercle pour chaque pièce
    OUTLINE = 2  # Contour de la pièce

    def __init__(self, row, col, color):
        # Initialise une pièce avec sa position et sa couleur
        self.row = row
        self.col = col
        self.color = color
        self.king = False  # Indicateur si la pièce est une dame
        self.x = 0  # Position X
        self.y = 0  # Position Y
        self.calc_pos()  # Calcule la position à l'écran

    def calc_pos(self):
        # Calcule la position (x, y) de la pièce en fonction de la ligne et de la colonne
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        # Met la pièce en dame
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
