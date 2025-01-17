#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : main.py
Authors : Gatien Clerc et Damien Garcia
Date    : 2025.01.17
Version : 0.4
Purpose : tout  ce qui est pour les piont
"""
#import
import pygame
from .constants import PION_1_bor, PION_2_bor, PION_1, PION_2, CROWN, SQUARE_SIZE, ROWS, COLS

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
        if self.color == PION_1:
            pygame.draw.circle(win, PION_1_bor, (self.x, self.y), radius + self.OUTLINE)  # Bordure du pion 1
            pygame.draw.circle(win, PION_1, (self.x, self.y), radius)  # Pièce colorée pour le pion 1
        elif self.color == PION_2:
            pygame.draw.circle(win, PION_2_bor, (self.x, self.y), radius + self.OUTLINE)  # Bordure du pion 2
            pygame.draw.circle(win, PION_2, (self.x, self.y), radius)  # Pièce colorée pour le pion 2

        if self.king:  # Si la pièce est une dame, afficher la couronne
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        # Déplace la pièce vers une nouvelle position
        self.row = row
        self.col = col
        self.calc_pos()  # Recalcule sa position (x, y)

    def get_valid_moves(self, piece):
        moves = {}
        directions = [
            (-1, -1),  # Haut-Gauche
            (-1, 1),  # Haut-Droit
            (1, -1),  # Bas-Gauche
            (1, 1),  # Bas-Droit
            (0, -1),  # Gauche
            (0, 1),  # Droit
            (-1, 0),  # Haut
            (1, 0)  # Bas
        ]

        for direction in directions:
            left = piece.col + direction[1]
            right = piece.col + direction[1]
            row = piece.row + direction[0]

            while 0 <= row < ROWS and 0 <= left < COLS and self.board[row][left] == 0:
                moves[(row, left)] = []  # La case est libre, on l'ajoute aux mouvements valides
                row += direction[0]
                left += direction[1]

            # Si une pièce adverse est trouvée, on peut sauter
            if 0 <= row < ROWS and 0 <= left < COLS and self.board[row][left] != 0 and self.board[row][
                left].color != piece.color:
                moves[(row, left)] = [self.board[row][left]]  # Ajout d'une pièce capturable
                row += direction[0]
                left += direction[1]

                while 0 <= row < ROWS and 0 <= left < COLS and self.board[row][left] == 0:
                    moves[(row, left)] = []  # Ajouter cette case comme une possibilité valide après la capture
                    row += direction[0]
                    left += direction[1]

        return moves

    def __repr__(self):
        # Représentation de la pièce
        return str(self.color)
