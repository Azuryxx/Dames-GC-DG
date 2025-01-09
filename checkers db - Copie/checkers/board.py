import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, WIDTH, HEIGHT
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        # Dessin de la bordure
        pygame.draw.rect(win, WHITE, (0, 0, WIDTH, HEIGHT), 5)  # Bordure blanche de 5 pixels

        # Dessin des cases
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

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
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 4:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 5:
                        self.board[row].append(Piece(row, col, RED))
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
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        # Détermine la limite en fonction du type de pièce
        max_distance = ROWS if piece.king else 3  # Reines illimitées, pions max 2 cases (3 lignes inclusives)

        # Si la pièce est une reine ou un pion rouge, elle peut se déplacer vers le haut
        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - max_distance, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - max_distance, -1), -1, piece.color, right))
        # Si la pièce est une reine ou un pion blanc, elle peut se déplacer vers le bas
        if piece.color == WHITE or piece.king:
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

