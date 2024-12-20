import pygame
from .constants import ROWS, COLS, CASE_FONCE, CASE_CLAIR, PION_1, PION_2
from .piece import Piece

class Board:
    def __init__(self):
        # Initialise le plateau et les variables de comptage des pièces
        self.board = []
        self.case_clair_left = self.case_fonce_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        # Dessine les cases du plateau
        win.fill(CASE_FONCE)  # Remplir la fenêtre avec la couleur de fond (CASE_FONCE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):  # Placer les cases claires et foncées
                pygame.draw.rect(win, CASE_CLAIR, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        # Crée le plateau et initialise les pièces
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 4:
                        self.board[row].append(Piece(row, col, PION_1))  # Pion 1
                    elif row > 5:
                        self.board[row].append(Piece(row, col, PION_2))  # Pion 2
                    else:
                        self.board[row].append(0)  # Case vide
                else:
                    self.board[row].append(0)  # Case vide

    def draw(self, win):
        # Dessine le plateau et les pièces
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def get_piece(self, row, col):
        # Récupère une pièce à la position (row, col)
        return self.board[row][col]

    def move(self, piece, row, col):
        # Déplace une pièce sur le plateau
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        # Promotion de la pièce en dame
        if row == ROWS - 1 or row == 0:
            piece.make_king()

    def winner(self):
        # Vérifie s'il y a un gagnant
        if self.case_fonce_left == 0:
            return PION_2  # Le joueur PION_2 gagne
        elif self.case_clair_left == 0:
            return PION_1  # Le joueur PION_1 gagne
        return None  # Pas encore de gagnant

    # Autres méthodes pour obtenir les mouvements valides, évaluer, etc.
