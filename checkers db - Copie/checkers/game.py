import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        # Dessiner les cases du plateau
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)

        # Dessiner la bordure autour de la zone de jeu (en dehors du plateau)
        border_color = (255, 0, 0)  # Couleur de la bordure (rouge dans ce cas)
        border_thickness = 10  # L'épaisseur de la bordure

        # Assurez-vous que la bordure ne chevauche pas le plateau
        pygame.draw.rect(self.win, border_color,
                         (0, 0, self.win.get_width(), border_thickness))  # Bordure en haut
        pygame.draw.rect(self.win, border_color,
                         (0, 0, border_thickness, self.win.get_height()))  # Bordure à gauche
        pygame.draw.rect(self.win, border_color,
                         (0, self.win.get_height() - border_thickness, self.win.get_width(),
                          border_thickness))  # Bordure en bas
        pygame.draw.rect(self.win, border_color,
                         (self.win.get_width() - border_thickness, 0, border_thickness,
                          self.win.get_height()))  # Bordure à droite

        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED  # Le joueur rouge commence
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
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
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()

    def display_turn(self):
        """Affiche le joueur dont c'est le tour."""
        font = pygame.font.SysFont("Arial", 40)
        turn_text = f"C'est au tour de {self.turn}"  # Affiche la couleur du joueur actuel
        text_surface = font.render(turn_text, True, (255, 255, 255))  # Texte blanc
        self.win.blit(text_surface, (10, 10))  # Affiche le texte en haut à gauche
