import pygame
from .constants import BLUE, PION_1, PION_2
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        # Réinitialise l'état du jeu
        self.selected = None
        self.board = Board()
        self.turn = PION_2  # Le joueur 2 commence
        self.valid_moves = {}

    def update(self):
        # Met à jour l'affichage du plateau et des mouvements valides
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def winner(self):
        # Récupère le gagnant du jeu
        return self.board.winner()

    def select(self, row, col):
        # Sélectionne une pièce ou effectue un mouvement
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        # Effectue un mouvement de la pièce sélectionnée
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        # Dessine les mouvements valides (cercles bleus)
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        # Change de tour entre PION_1 et PION_2
        self.valid_moves = {}
        if self.turn == PION_2:
            self.turn = PION_1
        else:
            self.turn = PION_2
