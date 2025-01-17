#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : main.py
Authors : Gatien Clerc et Damien Garcia
Date    : 2025.01.17
Version : 1.3
Purpose : gestion du gagnant
"""
#import
import pygame
import tkinter as tk
from tkinter import messagebox
from .constants import BLUE, SQUARE_SIZE,PION_1, PION_2,  HEIGHT, WIDTH, ROWS, COLS, BORDURE
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.pion1_left = self.pion2_left = 20  # Nombre de pièces restantes pour chaque couleurur
        self.pion1_kings = self.pion2_kings = 0  # Nombre de dames pour chaque couleur

    def update(self):
        # Dessiner les cases du plateau
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)

        # Vérifie s'il y a un gagnant
        winner_color = self.winner()  # Vérifie si un joueur a gagné
        if winner_color:
            self.display_winner(winner_color)  # Afficher le gagnant
            return  # Arrêter le jeu si un gagnant est trouvé

        # Dessiner la bordure autour de la zone de jeu (en dehors du plateau)
        border_color = BORDURE  # Couleur de la bordure (rouge dans ce cas)
        border = 10  # L'épaisseur de la bordure

        pygame.draw.rect(self.win, border_color,
                         (0, HEIGHT - 100, WIDTH, HEIGHT - 100), border)  # Bordure à droit

        pygame.display.update()


    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = PION_1  # Le joueur rouge commence
        self.valid_moves = {}

        # Ajoutez cette méthode à votre classe Game
        def display_winner(self, winner_color):
            """Affiche un message indiquant quel joueur a gagné dans une nouvelle fenêtre."""
            root = tk.Tk()
            root.title("Fin du jeu")

            # Définir un message selon le joueur qui a gagné
            if winner_color == PION_1:
                winner_text = "Le joueur Rouge a gagné!"
            elif winner_color == PION_2:
                winner_text = "Le joueur Blanc a gagné!"

            # Label pour afficher le gagnant
            label = tk.Label(root, text=winner_text, font=("Arial", 20), fg="black")
            label.pack(pady=20)

            # Fonction pour fermer la fenêtre de jeu ou retourner à la page d'accueil
            def on_quit():
                pygame.quit()  # Fermer pygame
                root.quit()  # Fermer la fenêtre Tkinter
                exit()  # Quitter le programme

            # Bouton pour quitter le jeu
            quit_button = tk.Button(root, text="Quitter", command=on_quit)
            quit_button.pack(pady=10)

            # Optionnel : bouton pour recommencer (vous pouvez l'ajouter si nécessaire)
            def restart_game():
                self.reset()  # Reset du jeu
                root.quit()  # Fermer la fenêtre Tkinter
                # Recommencer le jeu ou revenir au menu principal

            restart_button = tk.Button(root, text="Recommencer", command=restart_game)
            restart_button.pack(pady=10)

            # Lancer la fenêtre Tkinter
            root.mainloop()

    def winner(self):
        # Vérifie si un joueur n'a plus de pions
        if self.pion1_left <= 0:
            return PION_2  # Le joueur 2 (blanc) gagne
        elif self.pion2_left <= 0:
            return PION_1  # Le joueur 1 (rouge) gagne
        return None  # Si aucun joueur n'a gagné

    def is_piece_blocked(self, piece):
        valid_moves = self.get_valid_moves(piece)
        return len(valid_moves) == 0  # Si la pièce n'a pas de mouvement valide, elle est bloquée

    def reset(self):
        self._init()

    def select(self, row, col):
        """Sélectionne une pièce si c'est un pion du joueur actuel."""
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
        if self.turn == PION_1:
            self.turn = PION_2
        else:
            self.turn = PION_1


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

    # Initialiser pygame
    pygame.init()

    def display_winner(self, winner_color):
        """Affiche un message indiquant quel joueur a gagné."""
        font = pygame.font.SysFont("Arial", 40)

        if winner_color == PION_1:
            winner_text = "Le joueur Rouge a gagné!"
            text_color = (255, 0, 0)  # Rouge pour la couleur du texte
        elif winner_color == PION_2:
            winner_text = "Le joueur Blanc a gagné!"
            text_color = (255, 0, 0)  # Rouge pour la couleur du texte

        # Créer la surface avec le texte
        text_surface = font.render(winner_text, True, text_color)  # Texte en rouge
        # Centrer le texte à l'écran
        self.win.blit(text_surface,
                      (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))

        # Afficher l'écran
        pygame.display.update()

        # Attendre que l'utilisateur appuie sur une touche pour continuer ou fermer
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
