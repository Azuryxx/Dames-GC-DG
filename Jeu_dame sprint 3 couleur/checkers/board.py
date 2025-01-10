
from constants import PION_1, PION_2, ROWS, COLS, SQUARE_SIZE
from piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.create_board()

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
                        self.board[row].append(0)  # Case vide
                else:
                    self.board[row].append(0)  # Case vide

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == PION_1 or piece.king:
            moves.update(self._traverse_left(row - 1, -1, -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, -1, -1, piece.color, right))
        if piece.color == PION_2 or piece.king:
            moves.update(self._traverse_left(row + 1, 8, 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, 8, 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:  # Case vide
                if skipped:
                    moves[(r, left)] = skipped
                else:
                    moves[(r, left)] = skipped
            elif current.color != color:  # Case avec un pion adverse
                if not skipped:
                    skipped = [current]
                else:
                    break
            else:  # Case avec un pion de la même couleur
                break
            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        for r in range(start, stop, step):
            if right >= 8:
                break
            current = self.board[r][right]
            if current == 0:  # Case vide
                if skipped:
                    moves[(r, right)] = skipped
                else:
                    moves[(r, right)] = skipped
            elif current.color != color:  # Case avec un pion adverse
                if not skipped:
                    skipped = [current]
                else:
                    break
            else:  # Case avec un pion de la même couleur
                break
            right += 1
        return moves

    def move(self, piece, row, col):
        self.board[row][col] = piece
        self.board[piece.row][piece.col] = 0
        piece.row = row
        piece.col = col
        if (piece.color == PION_1 and piece.row == 0) or (piece.color == PION_2 and piece.row == 7):
            piece.make_king()
