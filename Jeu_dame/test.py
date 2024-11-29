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
pygame.display.set_caption("Dames")

# Chargement des images
background_image = pygame.image.load("bois.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pion_image_rose = pygame.image.load("donut_rose.png")
pion_image_rose = pygame.transform.scale(pion_image_rose, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_jaune = pygame.image.load("donut_jaune.png")
pion_image_jaune = pygame.transform.scale(pion_image_jaune, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_rose_renne = pygame.image.load("renne_rose.png")
pion_image_rose_renne = pygame.transform.scale(pion_image_rose_renne, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_jaune_renne = pygame.image.load("renne_jaune.png")
pion_image_jaune_renne = pygame.transform.scale(pion_image_jaune_renne, (SQUARE_SIZE, SQUARE_SIZE))

# Positions initiales des pions (x, y, couronne)
pions_rose = [(OFFSET + i * SQUARE_SIZE, OFFSET + j * SQUARE_SIZE, False) for j in range(4) for i in range(10) if (i + j) % 2 == 1]
pions_jaune = [(OFFSET + i * SQUARE_SIZE, OFFSET + (6 + j) * SQUARE_SIZE, False) for j in range(4) for i in range(10) if (i + j) % 2 == 1]

# Variables globales
running = True
selected_pion_index = None
current_player = "rose"

# Fonction pour dessiner le damier
def draw_checkerboard():
    for row in range(10):
        for col in range(10):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (OFFSET + col * SQUARE_SIZE, OFFSET + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Fonction pour dessiner la bordure
def draw_border():
    pygame.draw.rect(screen, WOOD_COLOR, (OFFSET - 5, OFFSET - 5, 10 * SQUARE_SIZE + 10, 10 * SQUARE_SIZE + 10), 5)

# Fonction pour dessiner le jeu
def draw_game():
    screen.blit(background_image, (0, 0))
    draw_border()
    draw_checkerboard()

    # Dessin des pions roses
    for x, y, couronne in pions_rose:
        if couronne:
            screen.blit(pion_image_rose_renne, (x, y))
        else:
            screen.blit(pion_image_rose, (x, y))

    # Dessin des pions jaunes
    for x, y, couronne in pions_jaune:
        if couronne:
            screen.blit(pion_image_jaune_renne, (x, y))
        else:
            screen.blit(pion_image_jaune, (x, y))

    # Affichage du joueur courant
    font = pygame.font.Font(None, 36)
    text = font.render(f"Joueur actuel : {current_player.capitalize()}", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))

    pygame.display.update()

# Fonction pour vérifier si un mouvement est possible
def can_move(new_x, new_y, all_pions):
    if not (OFFSET <= new_x < OFFSET + 10 * SQUARE_SIZE and OFFSET <= new_y < OFFSET + 10 * SQUARE_SIZE):
        return False
    return all((px, py) != (new_x, new_y) for px, py, _ in all_pions)

# Fonction pour capturer un pion
def capture_pion(px, py, new_x, new_y, opponent_pions):
    cx, cy = (px + new_x) // 2, (py + new_y) // 2  # Coordonnées du pion à capturer
    for i, (op_x, op_y, _) in enumerate(opponent_pions):
        if (op_x, op_y) == (cx, cy):  # Vérifie la correspondance exacte
            del opponent_pions[i]  # Supprime le pion capturé
            return True
    return False

# Boucle principale
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if current_player == "rose":
                for idx, (px, py, _) in enumerate(pions_rose):
                    if px <= x < px + SQUARE_SIZE and py <= y < py + SQUARE_SIZE:
                        selected_pion_index = idx
                        break
            else:
                for idx, (px, py, _) in enumerate(pions_jaune):
                    if px <= x < px + SQUARE_SIZE and py <= y < py + SQUARE_SIZE:
                        selected_pion_index = idx
                        break

        if event.type == pygame.KEYDOWN and selected_pion_index is not None:
            if current_player == "rose":
                pion = pions_rose[selected_pion_index]
                opponent_pions = pions_jaune
            else:
                pion = pions_jaune[selected_pion_index]
                opponent_pions = pions_rose

            px, py, couronne = pion
            new_x, new_y = px, py

            if event.key == pygame.K_RIGHT:
                new_x += SQUARE_SIZE
                new_y += -SQUARE_SIZE if current_player == "rose" else SQUARE_SIZE
            elif event.key == pygame.K_LEFT:
                new_x -= SQUARE_SIZE
                new_y += -SQUARE_SIZE if current_player == "rose" else SQUARE_SIZE

            # Vérification des mouvements valides
            if can_move(new_x, new_y, pions_rose + pions_jaune):
                # Vérification des captures
                if abs(new_x - px) == 2 * SQUARE_SIZE and abs(new_y - py) == 2 * SQUARE_SIZE:
                    if not capture_pion(px, py, new_x, new_y, opponent_pions):
                        continue

                # Couronnement
                if current_player == "rose" and new_y == OFFSET + 9 * SQUARE_SIZE:
                    couronne = True
                elif current_player == "jaune" and new_y == OFFSET:
                    couronne = True

                # Mise à jour du pion
                if current_player == "rose":
                    pions_rose[selected_pion_index] = (new_x, new_y, couronne)
                else:
                    pions_jaune[selected_pion_index] = (new_x, new_y, couronne)

                # Changement de joueur
                current_player = "jaune" if current_player == "rose" else "rose"
                selected_pion_index = None

    draw_game()

pygame.quit()
