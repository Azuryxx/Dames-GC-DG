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

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de dames")

# Chargement des images
background_image = pygame.image.load("bois.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pion_image_rose = pygame.image.load("donut_rose.png")
pion_image_rose = pygame.transform.scale(pion_image_rose, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_rose_promu = pygame.image.load("renne_rose.png")
pion_image_rose_promu = pygame.transform.scale(pion_image_rose_promu, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_jaune = pygame.image.load("donut_jaune.png")
pion_image_jaune = pygame.transform.scale(pion_image_jaune, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_jaune_promu = pygame.image.load("renne_jaune.png")
pion_image_jaune_promu = pygame.transform.scale(pion_image_jaune_promu, (SQUARE_SIZE, SQUARE_SIZE))

# Position initiale des pions
pions_rose = [{"pos": (OFFSET + 80, OFFSET), "promu": False},
              {"pos": (OFFSET + 80 * 3, OFFSET), "promu": False},
              {"pos": (OFFSET + 80 * 5, OFFSET), "promu": False},
              {"pos": (OFFSET + 80 * 7, OFFSET), "promu": False}]

pions_jaune = [{"pos": (OFFSET, OFFSET + 80 * 9), "promu": False},
               {"pos": (OFFSET + 80 * 2, OFFSET + 80 * 9), "promu": False},
               {"pos": (OFFSET + 80 * 4, OFFSET + 80 * 9), "promu": False},
               {"pos": (OFFSET + 80 * 6, OFFSET + 80 * 9), "promu": False}]

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

# Fonction pour afficher le plateau et les pions
def draw_game():
    screen.blit(background_image, (0, 0))
    draw_border()
    draw_checkerboard()

    # Affichage des pions roses
    for pion in pions_rose:
        px, py = pion["pos"]
        if pion["promu"]:
            screen.blit(pion_image_rose_promu, (px, py))
        else:
            screen.blit(pion_image_rose, (px, py))

    # Affichage des pions jaunes
    for pion in pions_jaune:
        px, py = pion["pos"]
        if pion["promu"]:
            screen.blit(pion_image_jaune_promu, (px, py))
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

# Fonction pour déplacer un pion
def move_pion(pion, dx, dy, all_pions):
    x, y = pion["pos"]
    new_x = x + dx * SQUARE_SIZE
    new_y = y + dy * SQUARE_SIZE

    if can_move(new_x, new_y, all_pions):
        pion["pos"] = (new_x, new_y)
        return True
    return False

# Fonction pour vérifier la promotion
def check_promotion(pion):
    x, y = pion["pos"]
    if current_player == "rose" and y == OFFSET + 9 * SQUARE_SIZE:  # Rose arrive en bas
        pion["promu"] = True
    elif current_player == "jaune" and y == OFFSET:  # Jaune arrive en haut
        pion["promu"] = True

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

                # Si c'est un pion promu, il peut se déplacer en diagonale
                if pion["promu"]:
                    if event.key == pygame.K_RIGHT:
                        move_pion(pion, 1, 1, pions_rose + pions_jaune)
                    elif event.key == pygame.K_LEFT:
                        move_pion(pion, -1, 1, pions_rose + pions_jaune)
                    elif event.key == pygame.K_DOWN:
                        move_pion(pion, 1, -1, pions_rose + pions_jaune)
                    elif event.key == pygame.K_UP:
                        move_pion(pion, -1, -1, pions_rose + pions_jaune)

                # Sinon, c'est un pion normal, il doit se déplacer d'une seule case
                else:
                    # Déplacements pour les pions non promus (vers l'avant)
                    if current_player == "rose":
                        if event.key == pygame.K_RIGHT:
                            move_pion(pion, 1, 1, pions_rose + pions_jaune)
                        elif event.key == pygame.K_LEFT:
                            move_pion(pion, -1, 1, pions_rose + pions_jaune)
                        elif event.key == pygame.K_DOWN:
                            move_pion(pion, 1, -1, pions_rose + pions_jaune)
                        elif event.key == pygame.K_UP:
                            move_pion(pion, -1, -1, pions_rose + pions_jaune)

                    elif current_player == "jaune":
                        if event.key == pygame.K_RIGHT:
                            move_pion(pion, 1, -1, pions_rose + pions_jaune)
                        elif event.key == pygame.K_LEFT:
                            move_pion(pion, -1, -1, pions_rose + pions_jaune)
                        elif event.key == pygame.K_DOWN:
                            move_pion(pion, 1, 1, pions_rose + pions_jaune)
                        elif event.key == pygame.K_UP:
                            move_pion(pion, -1, 1, pions_rose + pions_jaune)

                # Vérification de la promotion
                check_promotion(pion)

                # Changer de joueur
                current_player = "jaune" if current_player == "rose" else "rose"
                selected_pion_index = None

    draw_game()

pygame.quit()
