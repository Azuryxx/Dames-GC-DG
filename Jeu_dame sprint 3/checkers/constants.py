import pygame

# Dimensions de la fenêtre et des cases
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH // COLS  # Taille de chaque case

# Couleurs (en format RGB)
RED = (190, 190, 190, 255)  # Pion 2 et cases claires
WHITE = (160, 32, 240, 255)  # Pion 1
BLACK = (0, 0, 0)  # Cases foncées
BLUE = (0, 0, 255)  # Déplacement (mouvements valides)
GREY = (255, 0, 0, 255)  # Bordure des pions

# Couleurs spécifiques pour chaque type de pion
CASE_CLAIR = ("moccasin")
CASE_FONCE = ("saddlebrown")
PION_1 = ("deeppink")  # Pion 1
PION_2 = ("aquamarine")  # Pion 2
PION_1_bor = ("aquamarine")  # Bordure Pion 1
PION_2_bor = ("deeppink")  # Bordure Pion 2
BORDURE = ("olivedrab1")

# Image de la couronne pour les dames
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
