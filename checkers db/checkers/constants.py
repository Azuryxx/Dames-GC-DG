#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : main.py
Authors : Gatien Clerc et Damien Garcia
Date    : 2025.01.17
Version : 0.8
Purpose : tout les constantce
"""
#import
import pygame

# Taille de la bordure et dimensions de la fenêtre
WIDTH, HEIGHT = 650, 750
ROWS, COLS = 10, 10
SQUARE_SIZE = (WIDTH ) // COLS


# Dimensions totales de la fenêtre
WINDOW_WIDTH = WIDTH
WINDOW_HEIGHT = HEIGHT

#Couleurs
CASE_CLAIR = ("moccasin")
CASE_FONCE = ("saddlebrown")
PION_1 = ("deeppink")
PION_2 = ("aquamarine")
PION_1_bor = ("aquamarine")
PION_2_bor = ("deeppink")
BORDURE = ("white")
BLUE = (0, 0, 255)

FONT = ("arial", 12)
# Couronne
CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (20, 25))
