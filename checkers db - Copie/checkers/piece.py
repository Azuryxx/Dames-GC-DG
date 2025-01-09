from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN
import pygame


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False  # Indique si la pièce est une reine
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        """Calcule la position de la pièce sur le plateau."""
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        """Transforme la pièce en reine."""
        self.king = True

    def draw(self, win):
        """Dessine la pièce sur la fenêtre."""
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            # Dessiner la couronne si la pièce est une reine
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        """Déplace la pièce vers la nouvelle position."""
        self.row = row
        self.col = col
        self.calc_pos()

    def get_valid_moves(self, board):
        """Retourne les déplacements valides pour la pièce."""
        moves = []
        directions = []

        if self.king:
            # Si la pièce est une reine, elle peut se déplacer dans les 4 directions diagonales
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        else:
            # Le pion se déplace uniquement vers le bas ou vers le haut selon sa couleur
            directions = [(-1, -1), (-1, 1)] if self.color == RED else [(1, -1), (1, 1)]

        # Vérifie les mouvements dans chaque direction
        for direction in directions:
            row, col = self.row, self.col
            while True:
                row += direction[0]
                col += direction[1]
                if 0 <= row < 8 and 0 <= col < 8:  # Vérifie si la position est dans les limites du plateau
                    piece = board.get_piece(row, col)
                    if piece == 0:  # La case est vide, la pièce peut y aller
                        moves.append((row, col))
                    elif piece.color != self.color:  # Il y a un adversaire, la pièce peut capturer
                        moves.append((row, col))
                        break  # Arrêter dès qu'on rencontre une pièce adverse
                    else:
                        break  # La case est occupée par une pièce de la même couleur, on arrête
                else:
                    break  # La case est en dehors du plateau, on arrête
        return moves

    def __repr__(self):
        return f"Piece({self.color}, {self.row}, {self.col}, king={self.king})"
