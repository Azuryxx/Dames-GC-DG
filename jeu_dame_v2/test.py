import pygame
import os

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
pygame.display.set_caption("Jeu de Dames")

# Chargement de la police de type craie
chalk_font = pygame.font.Font("CoalhandLuke TRIAL.otf", 36)

# Chargement des images
background_image = pygame.image.load("bois.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pion_image_rose = pygame.image.load("donut_rose.png")
pion_image_rose = pygame.transform.scale(pion_image_rose, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_rose_renne = pygame.image.load("renne_rose.png")
pion_image_rose_renne = pygame.transform.scale(pion_image_rose_renne, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_jaune = pygame.image.load("donut_jaune.png")
pion_image_jaune = pygame.transform.scale(pion_image_jaune, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_jaune_renne = pygame.image.load("renne_jaune.png")
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

# Score des joueurs
score_rose = 0
score_jaune = 0

# Variables pour suivre la sélection et les déplacements
selected_pion = None
current_player = 'rose'
selected_pion_index = None

# Fonction pour enregistrer les scores dans un fichier
def save_scores():
    with open("scores.txt", "w") as f:
        f.write(f"Score Rose: {score_rose}\n")
        f.write(f"Score Jaune: {score_jaune}\n")

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
    text_red = chalk_font.render(f"Score Rouge: {score_rose}", True, RED)
    screen.blit(text_red, (OFFSET + box_width // 2 - text_red.get_width() // 2, box_y + box_height // 4))

    pygame.draw.rect(screen, SCORE_BOX_COLOR, (WIDTH - OFFSET - box_width, box_y, box_width, box_height))
    text_blue = chalk_font.render(f"Score Bleu: {score_jaune}", True, BLUE)
    screen.blit(text_blue, (WIDTH - OFFSET - box_width + box_width // 2 - text_blue.get_width() // 2,
                            box_y + box_height // 4))

# Fonction pour dessiner les pions
def draw_pions():
    for pion in pions_rose:
        px, py = pion["pos"]
        if pion["promu"]:
            screen.blit(pion_image_rose_renne, (px, py))
        else:
            screen.blit(pion_image_rose, (px, py))

    for pion in pions_jaune:
        px, py = pion["pos"]
        if pion["promu"]:
            screen.blit(pion_image_jaune_renne, (px, py))
        else:
            screen.blit(pion_image_jaune, (px, py))

# Fonction pour gérer la capture des pions
def capture_pion(captured_pion, pion_type):
    global score_rose, score_jaune
    if pion_type == 'rose':
        score_rose += 1
    else:
        score_jaune += 1
    captured_pion['pos'] = (-100, -100)  # Déplacer le pion capturé hors de l'écran
    save_scores()  # Sauvegarde les scores dans le fichier chaque fois qu'un pion est capturé

# Fonction pour vérifier si un mouvement est valide
def is_valid_move(pion, new_pos):
    return 0 <= new_pos[0] < WIDTH and 0 <= new_pos[1] < HEIGHT

# Fonction pour déplacer un pion avec capture
def move_pion_with_capture(pion, new_x, new_y, all_pions):
    # Vérifier s'il y a un pion à capturer
    for opponent_pion in all_pions:
        px, py = opponent_pion["pos"]
        if (new_x == px + SQUARE_SIZE and new_y == py + SQUARE_SIZE) or \
           (new_x == px - SQUARE_SIZE and new_y == py - SQUARE_SIZE):
            capture_pion(opponent_pion, "rose" if current_player == "jaune" else "jaune")
            return opponent_pion  # Retourner le pion capturé
    return None

# Fonction pour vérifier si le mouvement est possible
def can_move(new_x, new_y, all_pions):
    for pion in all_pions:
        px, py = pion["pos"]
        if px == new_x and py == new_y:
            return False
    return True
# Fonction pour dessiner le jeu
def draw_game():
    screen.blit(background_image, (0, 0))  # Dessiner l'image de fond (optionnel)
    draw_checkerboard()  # Dessiner le damier
    draw_border()  # Dessiner la bordure du plateau
    draw_score_boxes()  # Dessiner les cases de score
    draw_pions()  # Dessiner les pions

# Boucle principale du jeu
running = True
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
                    opponent_pions = pions_jaune
                else:
                    pions = pions_jaune
                    opponent_pions = pions_rose

                pion = pions[selected_pion_index]
                px, py = pion["pos"]
                new_x = px
                new_y = py

                # Si le pion est sélectionné, on le déplace uniquement en avant selon la direction
                if current_player == "rose":  # Pion rose ne va que vers le bas
                    if event.key == pygame.K_RIGHT:
                        new_x += SQUARE_SIZE
                        new_y += SQUARE_SIZE  # Diagonale droite vers l'avant

                    elif event.key == pygame.K_LEFT:
                        new_x -= SQUARE_SIZE
                        new_y += SQUARE_SIZE  # Diagonale gauche vers l'avant

                elif current_player == "jaune":  # Pion jaune ne va que vers le haut
                    if event.key == pygame.K_RIGHT:
                        new_x += SQUARE_SIZE
                        new_y -= SQUARE_SIZE  # Diagonale droite vers l'avant

                    elif event.key == pygame.K_LEFT:
                        new_x -= SQUARE_SIZE
                        new_y -= SQUARE_SIZE  # Diagonale gauche vers l'avant

                # Effectuer le mouvement avec capture si possible
                captured_pion = move_pion_with_capture(pion, new_x, new_y, pions_rose + pions_jaune)

                if captured_pion:
                    print(f"Pion capturé: {captured_pion}")

                # Vérifie si le mouvement est valide
                if can_move(new_x, new_y, pions_rose + pions_jaune):
                    pion["pos"] = (new_x, new_y)

                    # Promotion du pion
                    if current_player == "rose" and new_y == OFFSET + 9 * SQUARE_SIZE:
                        pion["promu"] = True
                    elif current_player == "jaune" and new_y == OFFSET:
                        pion["promu"] = True

                    # Changer de joueur
                    current_player = "jaune" if current_player == "rose" else "rose"
                    selected_pion_index = None  # Désélectionner le pion après son mouvement

                else:
                    print("Mouvement invalide")  # Optionnel, pour débogage

    draw_game()  # Appel à la fonction qui dessine le jeu

    pygame.display.update()

pygame.quit()