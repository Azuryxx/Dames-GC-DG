import pygame
from .constants import CASE_CLAIR, ROWS, SQUARE_SIZE, COLS, WIDTH, HEIGHT, PION_1, PION_2, CASE_FONCE
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.pion_I_left = self.pion_II_left = 12
        self.pion_I_kings = self.pion_II_kings = 0
        self.create_board()

    def draw_squares(self, win):
        """Dessine les cases du plateau avec des couleurs alternées."""
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:  # Alterne entre clair et foncé
                    color = CASE_CLAIR
                else:
                    color = CASE_FONCE
                pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        return self.pion_II_left- self.pion_I_left + (self.pion_II_kings * 0.5 - self.pion_I_kings * 0.5)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        # Transformer en roi si atteint le bord opposé
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == PION_2:
                self.pion_II_kings += 1
            else:
                self.pion_I_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])  # Crée une nouvelle ligne sur le plateau
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):  # Alterne les cases
                    if row < 3:  # Les pions bleus (PION_2) sont dans les 3 premières lignes
                        self.board[row].append(Piece(row, col, PION_2))  # Bleu
                    elif row > 4:  # Les pions roses (PION_1) sont dans les 3 dernières lignes
                        self.board[row].append(Piece(row, col, PION_1))  # Rose
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            if piece != 0:
                print(f"Removing piece at ({piece.row}, {piece.col})")
                self.board[piece.row][piece.col] = 0
                if piece.color == PION_1:
                    self.pion_I_left -= 1
                else:
                    self.pion_II_left -= 1

    def winner(self):
        if self.pion_I_left <= 0:
            return PION_2
        elif self.pion_II_left <= 0:
            return PION_1
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        # Détermine la limite en fonction du type de pièce
        max_distance = ROWS if piece.king else 3  # Reines illimitées, pions max 2 cases (3 lignes inclusives)

        # Si la pièce est une reine ou un pion rouge, elle peut se déplacer vers le haut
        if piece.color == PION_1 or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - max_distance, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - max_distance, -1), -1, piece.color, right))
        # Si la pièce est une reine ou un pion blanc, elle peut se déplacer vers le bas
        if piece.color == PION_2 or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + max_distance, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + max_distance, ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        distance = 0  # Compteur pour limiter les déplacements à 2 cases maximum

        while 0 <= left < COLS and start != stop and distance < 3:  # Limite à 2 cases (3 lignes inclusives)
            current = self.board[start][left]

            if current == 0:  # Case vide
                if skipped and not last:
                    break
                elif skipped:
                    moves[(start, left)] = last + skipped
                else:
                    moves[(start, left)] = last
            elif current.color == color:  # Si la case contient une pièce de la même couleur
                break
            else:  # Une pièce adverse, on peut la sauter
                last = [current]

            start += step
            left -= 1  # Avancer sur la diagonale gauche
            distance += 1  # Incrémenter la distance parcourue

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        distance = 0  # Compteur pour limiter les déplacements à 2 cases maximum

        while 0 <= right < COLS and start != stop and distance < 3:  # Limite à 2 cases (3 lignes inclusives)
            current = self.board[start][right]

            if current == 0:  # Case vide
                if skipped and not last:
                    break
                elif skipped:
                    moves[(start, right)] = last + skipped
                else:
                    moves[(start, right)] = last
            elif current.color == color:  # Si la case contient une pièce de la même couleur
                break
            else:  # Une pièce adverse, on peut la sauter
                last = [current]

            start += step
            right += 1  # Avancer sur la diagonale droite
            distance += 1  # Incrémenter la distance parcourue

        return moves

