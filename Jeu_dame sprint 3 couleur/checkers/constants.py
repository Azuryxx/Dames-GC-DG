import pygame

# Dimensions de la fenêtre et des cases
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH // COLS  # Taille de chaque case


BLUE = (0, 0, 255)  # Déplacement (mouvements valides)

# Couleurs spécifiques pour chaque type de pion
CASE_CLAIR = ("moccasin")
CASE_FONCE = ("saddlebrown")
PION_1 = ("deeppink")  # Pion 1
PION_2 = ("aquamarine")  # Pion 2
PION_1_bor = ("aquamarine")  # Bordure Pion 1
PION_2_bor = ("deeppink")  # Bordure Pion 2
BORDURE = ("black")

# Image de la couronne pour les dames
CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (20, 25))
