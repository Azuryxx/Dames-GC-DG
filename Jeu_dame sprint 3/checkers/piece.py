import pygame
from .constants import SQUARE_SIZE, GREY, CROWN

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

    def draw(self, win):
        # Dessine la pièce sur l'écran
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)  # Contour
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)  # Pièce colorée
        if self.king:  # Si la pièce est une dame, afficher la couronne
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        # Déplace la pièce vers une nouvelle position
        self.row = row
        self.col = col
        self.calc_pos()  # Recalcule sa position (x, y)

    def __repr__(self):
        # Représentation de la pièce
        return str(self.color)
