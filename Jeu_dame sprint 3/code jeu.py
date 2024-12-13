import pygame

# Initialisation de pygame
pygame.init()

# Taille de la fenêtre
WIDTH = 1000
HEIGHT = 1000
OFFSET = 100

# Taille des cases
SQUARE_SIZE = (WIDTH - 2 * OFFSET) // 10

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WOOD_COLOR = (139, 69, 19)
SCORE_BOX_COLOR = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ma-24-DG-GC")

# Chargement de la police de type craie
chalk_font = pygame.font.Font("CoalhandLuke TRIAL 1.otf", 36)

# Chargement des images
background_image = pygame.image.load("bois.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pion_image_rose = pygame.image.load("pion_donut_rose.png")
pion_image_rose = pygame.transform.scale(pion_image_rose, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_rose_renne = pygame.image.load("renne_donut_rose.png")
pion_image_rose_renne = pygame.transform.scale(pion_image_rose_renne, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_jaune = pygame.image.load("pion_donut_jaune.png")
pion_image_jaune = pygame.transform.scale(pion_image_jaune, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_jaune_renne = pygame.image.load("renne_donut_jaune.png")
pion_image_jaune_renne = pygame.transform.scale(pion_image_jaune_renne, (SQUARE_SIZE, SQUARE_SIZE))

# Position initiale des pions
pions_rose = [
    {"pos": (OFFSET + 80, OFFSET), "promu": False},
    {"pos": (OFFSET + 80 * 3, OFFSET), "promu": False},
    {"pos": (OFFSET + 80 * 5, OFFSET), "promu": False},
    {"pos": (OFFSET + 80 * 7, OFFSET), "promu": False},
    {"pos": (OFFSET + 80 * 9, OFFSET), "promu": False},
    {"pos": (OFFSET + 0, OFFSET + 80), "promu": False},
    {"pos": (OFFSET + 80 * 2, OFFSET + 80), "promu": False},
    {"pos": (OFFSET + 80 * 4, OFFSET + 80), "promu": False},
    {"pos": (OFFSET + 80 * 6, OFFSET + 80), "promu": False},
    {"pos": (OFFSET + 80 * 8, OFFSET + 80), "promu": False},
    {"pos": (OFFSET + 80, OFFSET + 80 * 2), "promu": False},
    {"pos": (OFFSET + 80 * 3, OFFSET + 80 * 2), "promu": False},
    {"pos": (OFFSET + 80 * 5, OFFSET + 80 * 2), "promu": False},
    {"pos": (OFFSET + 80 * 7, OFFSET + 80 * 2), "promu": False},
    {"pos": (OFFSET + 80 * 9, OFFSET + 80 * 2), "promu": False},
    {"pos": (OFFSET + 0, OFFSET + 80 * 3 ), "promu": False},
    {"pos": (OFFSET + 80 * 2, OFFSET + 80 * 3), "promu": False},
    {"pos": (OFFSET + 80 * 4, OFFSET + 80 * 3), "promu": False},
    {"pos": (OFFSET + 80 * 6, OFFSET + 80 * 3), "promu": False},
    {"pos": (OFFSET + 80 * 8, OFFSET + 80 * 3), "promu": False}
]

pions_jaune = [
    {"pos": (OFFSET + 80, OFFSET + 80 * 6), "promu": False},
    {"pos": (OFFSET + 80 * 3, OFFSET + 80 * 6), "promu": False},
    {"pos": (OFFSET + 80 * 5, OFFSET + 80 * 6), "promu": False},
    {"pos": (OFFSET + 80 * 7, OFFSET + 80 * 6), "promu": False},
    {"pos": (OFFSET + 80 * 9, OFFSET + 80 * 6), "promu": False},
    {"pos": (OFFSET + 0, OFFSET + 80 * 7), "promu": False},
    {"pos": (OFFSET + 80 * 2, OFFSET + 80 * 7), "promu": False},
    {"pos": (OFFSET + 80 * 4, OFFSET + 80 * 7), "promu": False},
    {"pos": (OFFSET + 80 * 6, OFFSET + 80 * 7), "promu": False},
    {"pos": (OFFSET + 80 * 8, OFFSET + 80 * 7), "promu": False},
    {"pos": (OFFSET + 80, OFFSET + 80 * 8), "promu": False},
    {"pos": (OFFSET + 80 * 3, OFFSET + 80 * 8), "promu": False},
    {"pos": (OFFSET + 80 * 5, OFFSET + 80 * 8), "promu": False},
    {"pos": (OFFSET + 80 * 7, OFFSET + 80 * 8), "promu": False},
    {"pos": (OFFSET + 80 * 9, OFFSET + 80 * 8), "promu": False},
    {"pos": (OFFSET + 0, OFFSET + 80 * 9), "promu": False},
    {"pos": (OFFSET + 80 * 2, OFFSET + 80 * 9), "promu": False},
    {"pos": (OFFSET + 80 * 4, OFFSET + 80 * 9), "promu": False},
    {"pos": (OFFSET + 80 * 6, OFFSET + 80 * 9), "promu": False},
    {"pos": (OFFSET + 80 * 8, OFFSET + 80 * 9), "promu": False}
]

# Fonction pour dessiner le damier
def draw_checkerboard():
    for row in range(10):
        for col in range(10):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color,
                             (OFFSET + col * SQUARE_SIZE, OFFSET + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Fonction pour dessiner la bordure
def draw_border():
    pygame.draw.rect(screen, WOOD_COLOR, (OFFSET - 5, OFFSET - 5, 10 * SQUARE_SIZE + 10, 10 * SQUARE_SIZE + 10), 5)

# Fonction pour dessiner les cases de score
def draw_score_boxes():
    box_width = SQUARE_SIZE * 4
    box_height = SQUARE_SIZE
    box_y = OFFSET + 10 * SQUARE_SIZE + 10

    pygame.draw.rect(screen, SCORE_BOX_COLOR, (OFFSET, box_y, box_width, box_height))
    text_red = chalk_font.render("Score Rouge: 0", True, RED)
    screen.blit(text_red, (OFFSET + box_width // 2 - text_red.get_width() // 2, box_y + box_height // 4))

    pygame.draw.rect(screen, SCORE_BOX_COLOR, (WIDTH - OFFSET - box_width, box_y, box_width, box_height))
    text_blue = chalk_font.render("Score Bleu: 0", True, BLUE)
    screen.blit(text_blue, (WIDTH - OFFSET - box_width + box_width // 2 - text_blue.get_width() // 2, box_y + box_height // 4))

# Fonction pour afficher le plateau et les pions
def draw_game():
    screen.blit(background_image, (0, 0))
    draw_border()
    draw_checkerboard()
    draw_score_boxes()

    # Affichage des pions roses
    for pion in pions_rose:
        px, py = pion["pos"]
        if pion["promu"]:
            screen.blit(pion_image_rose_renne, (px, py))
        else:
            screen.blit(pion_image_rose, (px, py))

    # Affichage des pions jaunes
    for pion in pions_jaune:
        px, py = pion["pos"]
        if pion["promu"]:
            screen.blit(pion_image_jaune_renne, (px, py))
        else:
            screen.blit(pion_image_jaune, (px, py))

    pygame.display.flip()

# Fonction pour vérifier si un mouvement est possible
def can_move(new_x, new_y, all_pions):
    min_x = OFFSET
    max_x = OFFSET + 9 * SQUARE_SIZE
    min_y = OFFSET
    max_y = OFFSET + 9 * SQUARE_SIZE

    if not (min_x <= new_x <= max_x and min_y <= new_y <= max_y):
        return False  # Le mouvement est hors des limites

    # Vérifie qu'il n'y a pas déjà un pion à la position cible
    for pion in all_pions:
        if pion["pos"] == (new_x, new_y):
            return False  # Un autre pion occupe déjà cette position

    return True  # Le mouvement est valide

# Boucle principale du jeu
running = True
selected_pion_index = None
current_player = "rose"  # Joueur qui joue en premier

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # Chercher si un pion a été cliqué
            selected_pion_index = None
            if current_player == "rose":
                for idx, pion in enumerate(pions_rose):
                    px, py = pion["pos"]
                    if px <= x <= px + SQUARE_SIZE and py <= y <= py + SQUARE_SIZE:
                        selected_pion_index = idx
                        break
            else:
                for idx, pion in enumerate(pions_jaune):
                    px, py = pion["pos"]
                    if px <= x <= px + SQUARE_SIZE and py <= y <= py + SQUARE_SIZE:
                        selected_pion_index = idx
                        break

        if event.type == pygame.KEYDOWN:
            if selected_pion_index is not None:
                # Déterminer le pion sélectionné
                if current_player == "rose":
                    pions = pions_rose
                else:
                    pions = pions_jaune

                pion = pions[selected_pion_index]
                px, py = pion["pos"]
                new_x = px
                new_y = py

                # Déplacer le pion en diagonale
                if event.key == pygame.K_RIGHT:
                    new_x += SQUARE_SIZE
                    new_y += SQUARE_SIZE

                elif event.key == pygame.K_LEFT:
                    new_x -= SQUARE_SIZE
                    new_y -= SQUARE_SIZE

                elif event.key == pygame.K_DOWN:
                    new_x -= SQUARE_SIZE
                    new_y += SQUARE_SIZE

                elif event.key == pygame.K_UP:

                    new_x += SQUARE_SIZE
                    new_y -= SQUARE_SIZE

                # Vérifie si le mouvement est possible
                if can_move(new_x, new_y, pions_rose + pions_jaune):
                    pion["pos"] = (new_x, new_y)

                    # Promotion du pion
                    if current_player == "rose" and new_y == OFFSET + 9 * SQUARE_SIZE:
                        pion["promu"] = True
                    elif current_player == "jaune" and new_y == OFFSET:
                        pion["promu"] = True

                    # Changer de joueur
                    current_player = "jaune" if current_player == "rose" else "rose"
                    selected_pion_index = None

    draw_game()

pygame.quit()
