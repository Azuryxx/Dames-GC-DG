import  pygame
from .constants import CASE_CLAIR, CASE_FONCE, ROWS, COLS, SQUARE_SIZE, PION_1, PION_2, WIDTH, HEIGHT, FONT
from .piece import Piece

class Board:
    def __init__(self):
        # Initialisation des variables de jeu
        self.board = []
        self.red_left = self.white_left = 12  # Nombre de pièces restantes pour chaque couleur
        self.red_kings = self.white_kings = 0  # Nombre de dames pour chaque couleur
        self.create_board()  # Création du plateau de jeu

    def draw_squares(self, win):
        # Dessine les cases du plateau
        win.fill(CASE_FONCE)  # Remplir le fond avec la couleur foncée
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):  # Remplir les cases alternées (cases noires)
                pygame.draw.rect(win, CASE_CLAIR, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        # Retourne l'évaluation du plateau basé sur le nombre de pièces et de dames
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

    def get_all_pieces(self, color):
        # Retourne toutes les pièces d'une couleur donnée
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:  # Si la case contient une pièce de la couleur spécifiée
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        # Déplace une pièce d'une case à une autre
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)  # Met à jour la position de la pièce

        # Vérifie si la pièce a atteint la dernière ligne pour devenir une dame
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == PION_2:
                self.white_kings += 1  # Incrémente le nombre de dames blanches
            else:
                self.red_kings += 1  # Incrémente le nombre de dames rouges

    def get_piece(self, row, col):
        # Retourne la pièce à une position donnée
        return self.board[row][col]

    def draw_turn(win, turn_color):
        """Affiche le tour du joueur en bas du damier"""
        text = FONT.render(f"Tour de: {turn_color}", True, (255, 255, 255))  # Texte en blanc
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 50))  # Positionner le texte au centre en bas


    def create_board(self):
        # Crée un plateau avec les pièces initiales placées sur les cases appropriées
        for row in range(ROWS):
            self.board.append([])  # Crée une nouvelle ligne sur le plateau
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):  # Alterne les cases
                    if row < 4:  # Les pièces rouges (PION_2) sont dans les 4 premières lignes
                        self.board[row].append(Piece(row, col, PION_2))
                    elif row > 5:  # Les pièces blanches (PION_1) sont dans les 4 dernières lignes
                        self.board[row].append(Piece(row, col, PION_1))
                    else:
                        self.board[row].append(0)  # Case vide
                else:
                    self.board[row].append(0)  # Case vide

    def draw(self, win):
        # Dessine le plateau et toutes les pièces
        self.draw_squares(win)  # Dessine les cases du plateau
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:  # Si la case contient une pièce, dessiner la pièce
                    piece.draw(win)

    def remove(self, pieces):
        # Enlève les pièces capturées du plateau
        for piece in pieces:
            self.board[piece.row][piece.col] = 0  # La case devient vide
            if piece != 0:
                if piece.color == PION_1:
                    self.red_left -= 1  # Décrémente le nombre de pièces rouges restantes
                else:
                    self.white_left -= 1  # Décrémente le nombre de pièces blanches restantes

    def winner(self):
        # Retourne le gagnant du jeu
        if self.red_left <= 0:
            return PION_2  # Le joueur 2 (blanc) gagne
        elif self.white_left <= 0:
            return PION_1  # Le joueur 1 (rouge) gagne

        return None  # Si aucun joueur n'a gagné

    def get_valid_moves(self, piece):
        # Retourne les mouvements valides pour une pièce donnée
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == PION_1 or piece.king:
            moves.update(self._traverse_left(row - 1, -1, -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, -1, -1, piece.color, right))
        if piece.color == PION_2 or piece.king:
            moves.update(self._traverse_left(row + 1, ROWS, 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, ROWS, 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        # Traverse vers la gauche à partir d'une position donnée
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:  # Si la colonne est invalide, sortir
                break

            current = self.board[r][left]
            if current == 0:
                # Si la case est vide, enregistrer le mouvement possible
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:  # Si des pièces ont été sautées
                    moves.update(self._traverse_left(r + step, stop, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, stop, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break  # Si une pièce de la même couleur est trouvée, arrêter
            else:
                last = [current]  # Marquer la pièce comme étant sautée

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        # Traverse vers la droite à partir d'une position donnée
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:  # Si la colonne est invalide, sortir
                break

            current = self.board[r][right]
            if current == 0:
                # Si la case est vide, enregistrer le mouvement possible
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:  # Si des pièces ont été sautées
                    moves.update(self._traverse_left(r + step, stop, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, stop, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break  # Si une pièce de la même couleur est trouvée, arrêter
            else:
                last = [current]  # Marquer la pièce comme étant sautée

            right += 1

        return moves
