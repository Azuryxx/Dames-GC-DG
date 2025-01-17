#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : board.py
Authors : Gatien Clerc et Damien Garcia
Date    : 2025.01.17
Version : 0.07
Purpose : gestion des mouvement et de la fichage
"""
#import
import  pygame
from .constants import CASE_CLAIR, CASE_FONCE, ROWS, COLS, SQUARE_SIZE, PION_1, PION_2, WIDTH, HEIGHT,BLUE
from .piece import Piece

class Board:
    def __init__(self):
        # Initialisation des variables de jeu
        self.board = []
        self.turn_color = PION_1  # Le joueur qui commence
        self.create_board()  # Création du plateau de jeu
        self.pion1_left = self.pion2_left = 20  # Nombre de pièces restantes pour chaque couleurur
        self.pion1_kings = self.pion2_kings = 0  # Nombre de dames pour chaque couleur

    def draw_squares(self, win):
        # Dessine les cases du plateau
        win.fill(CASE_FONCE)  # Remplir le fond avec la couleur foncée
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):  # Remplir les cases alternées (cases noires)
                pygame.draw.rect(win, CASE_CLAIR, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        # Retourne l'évaluation du plateau basé sur le nombre de pièces et de dames
        return self.pion2_left - self.pion1_left + (self.pion2_kings * 0.5 - self.pion1_kings * 0.5)

    def get_all_pieces(self, color):
        # Retourne toutes les pièces d'une couleur donnée
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:  # Si la case contient une pièce de la couleur spécifiée
                    pieces.append(piece)
        return pieces

    def check_victory(self):
        # Vérifier si l'un des joueurs a gagné en n'ayant plus de pions
        if self.pion1_left == 0:
            self.display_winner("Joueur 2")  # Joueur 2 gagne
            return True
        elif self.pion2_left == 0:
            self.display_winner("Joueur 1")  # Joueur 1 gagne
            return True

        # Vérifier si un joueur ne peut plus bouger
        if self.can_player_move(PION_1) == False:
            self.display_winner("Joueur 2")  # Joueur 2 gagne
            return True
        elif self.can_player_move(PION_2) == False:
            self.display_winner("Joueur 1")  # Joueur 1 gagne
            return True

        return False

    def display_winner(self, winner):
        # Affiche un message de victoire à l'écran
        font = pygame.font.Font(None, 36)
        text = font.render(f"{winner} a gagné!", True, BLUE)
        screen = pygame.display.get_surface()
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(10000)  # Attendre 2 secondes avant de quitter

    def can_player_move(self, player_color):
        def can_player_move(self, player_color):
            # Vérifie si le joueur peut effectuer un mouvement
            for row in range(ROWS):
                for col in range(COLS):
                    piece = self.board[row][col]
                    if piece and piece.color == player_color:
                        # Vérifie si la pièce peut se déplacer
                        valid_moves = piece.get_valid_moves(self)
                        if valid_moves:
                            return True  # Si un mouvement valide est trouvé
            return False  # Aucun mouvement valide trouvé

    def move(self, piece, row, col):
        # Déplace une pièce d'une case à une autre
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)  # Met à jour la position de la pièce

        # Vérifie si la pièce a atteint la dernière ligne pour devenir une dame
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == PION_2:
                self.pion2_kings += 1  # Incrémente le nombre de dames blanches
            else:
                self.pion1_kings += 1  # Incrémente le nombre de dames rouges

        # Vérifier si un joueur a gagné après chaque mouvement
        if self.check_victory():
            return  # La partie est terminée si un joueur a gagné

    def get_piece(self, row, col):
        # Retourne la pièce à une position donnée
        return self.board[row][col]

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
                    self.pion1_left -= 1  # Décrémente le nombre de pièces rouges restantes
                else:
                    self.pion2_left -= 1  # Décrémente le nombre de pièces blanches restantes


    def get_valid_moves(self, piece):
        moves = {}

        if piece.king:
            # Si la pièce est une reine, nous utilisons les nouvelles fonctions de traversée pour chaque diagonale
            moves.update(self._traverse_left_queen(piece.row - 1, -1, -1, piece.color, piece.col - 1))
            moves.update(self._traverse_right_queen(piece.row - 1, -1, -1, piece.color, piece.col + 1))
            moves.update(self._traverse_left_queen(piece.row + 1, ROWS, 1, piece.color, piece.col - 1))
            moves.update(self._traverse_right_queen(piece.row + 1, ROWS, 1, piece.color, piece.col + 1))
        else:
            # Déplacements classiques pour les pions (mouvement sur 1 case dans une direction)
            if piece.color == PION_1 or piece.king:
                moves.update(self._traverse_left(piece.row - 1, -1, -1, piece.color, piece.col - 1))
                moves.update(self._traverse_right(piece.row - 1, -1, -1, piece.color, piece.col + 1))
            if piece.color == PION_2 or piece.king:
                moves.update(self._traverse_left(piece.row + 1, ROWS, 1, piece.color, piece.col - 1))
                moves.update(self._traverse_right(piece.row + 1, ROWS, 1, piece.color, piece.col + 1))

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

    def _traverse_left_queen(self, start_row, stop_row, step, color, start_col, skipped=[]):
        """Fonction pour gérer les mouvements à gauche pour une reine avec la possibilité de capturer plusieurs pièces"""
        moves = {}
        row = start_row
        col = start_col
        while 0 <= row < ROWS and 0 <= col < COLS:
            current = self.board[row][col]
            if current == 0:  # Case vide
                if skipped:  # Si une pièce a été sautée
                    moves[(row, col)] = skipped  # Ajouter le mouvement avec les pièces capturées
                else:
                    moves[(row, col)] = []  # Ajouter le mouvement sans capture
            elif current.color == color:  # Une pièce de la même couleur
                break  # Arrêter si une pièce de la même couleur est rencontrée
            else:  # Une pièce ennemie, elle peut être capturée
                next_row = row + step
                next_col = col - 1
                if 0 <= next_row < ROWS and 0 <= next_col < COLS and self.board[next_row][next_col] == 0:
                    # Vérifier si la case suivante est vide pour pouvoir capturer
                    moves.update(
                        self._traverse_left_queen(next_row, stop_row, step, color, next_col, skipped + [current]))
                break
            row += step
            col -= 1
        return moves

    def _traverse_right_queen(self, start_row, stop_row, step, color, start_col, skipped=[]):
        """Fonction pour gérer les mouvements à droite pour une reine avec la possibilité de capturer plusieurs pièces"""
        moves = {}
        row = start_row
        col = start_col
        while 0 <= row < ROWS and 0 <= col < COLS:
            current = self.board[row][col]
            if current == 0:  # Case vide
                if skipped:  # Si une pièce a été sautée
                    moves[(row, col)] = skipped  # Ajouter le mouvement avec les pièces capturées
                else:
                    moves[(row, col)] = []  # Ajouter le mouvement sans capture
            elif current.color == color:  # Une pièce de la même couleur
                break  # Arrêter si une pièce de la même couleur est rencontrée
            else:  # Une pièce ennemie, elle peut être capturée
                next_row = row + step
                next_col = col + 1
                if 0 <= next_row < ROWS and 0 <= next_col < COLS and self.board[next_row][next_col] == 0:
                    # Vérifier si la case suivante est vide pour pouvoir capturer
                    moves.update(
                        self._traverse_right_queen(next_row, stop_row, step, color, next_col, skipped + [current]))
                break
            row += step
            col += 1
        return moves