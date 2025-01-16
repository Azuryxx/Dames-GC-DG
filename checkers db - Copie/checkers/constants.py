import pygame

# Taille de la bordure et dimensions de la fenêtre
WIDTH, HEIGHT = 650, 750
ROWS, COLS = 10, 10
SQUARE_SIZE = (WIDTH ) // COLS


# Dimensions totales de la fenêtre
WINDOW_WIDTH = WIDTH
WINDOW_HEIGHT = HEIGHT

FONT = ("arial", 12)

#Couleurs
CASE_CLAIR = ("moccasin")
CASE_FONCE = ("saddlebrown")
PION_1 = ("deeppink")
PION_2 = ("aquamarine")
PION_1_bor = ("aquamarine")
PION_2_bor = ("deeppink")
BORDURE = ("white")
BLUE = (0, 0, 255)


# Couronne
CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (20, 25))
