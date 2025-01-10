import pygame

# Taille de la bordure
BORDER_SIZE = 100

# Dimensions totales de la fenêtre (inchangées)
WIDTH, HEIGHT = 1000, 1000

# Paramètres du damier
ROWS, COLS = 10, 10
BORDER_SIZE = 100  # Taille de la bordure autour du damier
SQUARE_SIZE = (WIDTH - 2 * BORDER_SIZE) // COLS  # Taille des cases

# Dimensions totales de la fenêtre
WINDOW_WIDTH = WIDTH + 2 * BORDER_SIZE
WINDOW_HEIGHT = HEIGHT + 2 * BORDER_SIZE

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