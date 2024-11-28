import pygame

# Initialisation de pygame
pygame.init()

# Taille de la fenêtre
WIDTH = 1000  # Largeur de la fenêtre
HEIGHT = 1000  # Hauteur de la fenêtre
OFFSET = 100  # Décalage des cases

# Taille des cases
SQUARE_SIZE = (WIDTH - 2 * OFFSET) // 10  # 10 cases de largeur

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WOOD_COLOR = (139, 69, 19)  # Couleur bois
SCORE_BOX_COLOR = (200, 200, 200)  # Couleur des cases de score
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ma-24-DG-GC")

# Chargement de la police de type craie
chalk_font = pygame.font.Font("CoalhandLuke TRIAL.otf", 36)

# Chargement de l'image de fond et du pion
background_image = pygame.image.load("bois.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pion_image = pygame.image.load("pngimg.com - donut_PNG63 (1).png")
pion_image = pygame.transform.scale(pion_image, (SQUARE_SIZE, SQUARE_SIZE))

# Position initiale du pion
pion_x = OFFSET + 80
pion_y = OFFSET


# Fonction pour dessiner le damier (10x10)
def draw_checkerboard():
    for row in range(10):
        for col in range(10):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color,
                             (OFFSET + col * SQUARE_SIZE, OFFSET + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

####oui
# Fonction pour dessiner la bordure en bois autour du damier
def draw_border():
    pygame.draw.rect(screen, WOOD_COLOR, (OFFSET - 5, OFFSET - 5, 10 * SQUARE_SIZE + 10, 10 * SQUARE_SIZE + 10), 5)


# Fonction pour dessiner les cases de score
def draw_score_boxes():
    # Taille des cases de score
    box_width = SQUARE_SIZE * 4
    box_height = SQUARE_SIZE
    box_y = OFFSET + 10 * SQUARE_SIZE + 10  # Position Y sous le damier

    # Case pour le score du joueur rouge (à gauche)
    pygame.draw.rect(screen, SCORE_BOX_COLOR, (OFFSET, box_y, box_width, box_height))
    text_red = chalk_font.render("Score Rouge: 0", True, RED)
    screen.blit(text_red, (OFFSET + box_width // 2 - text_red.get_width() // 2, box_y + box_height // 4))

    # Case pour le score du joueur bleu (à droite)
    pygame.draw.rect(screen, SCORE_BOX_COLOR, (WIDTH - OFFSET - box_width, box_y, box_width, box_height))
    text_blue = chalk_font.render("Score Bleu: 0", True, BLUE)
    screen.blit(text_blue,
                (WIDTH - OFFSET - box_width + box_width // 2 - text_blue.get_width() // 2, box_y + box_height // 4))


# Fonction pour vérifier si un mouvement est possible
def can_move(new_x, new_y):
    min_x = OFFSET
    max_x = OFFSET + 9 * SQUARE_SIZE
    min_y = OFFSET
    max_y = OFFSET + 9 * SQUARE_SIZE
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Définir la nouvelle position potentielle
            new_x = pion_x
            new_y = pion_y

            if event.type == pygame.KEYDOWN:
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

            # Vérifier si le mouvement est autorisé
            if can_move(new_x, new_y):
                pion_x = new_x
                pion_y = new_y
            else:
                # Afficher un message d'erreur dans la console
                print("Erreur : Mouvement impossible, vous êtes au bord du damier !")

    # Afficher l'image de fond
    screen.blit(background_image, (0, 0))

    # Dessiner la bordure
    draw_border()

    # Dessiner le damier
    draw_checkerboard()

    # Dessiner les cases de score
    draw_score_boxes()

    # Dessiner le pion à sa position actuelle
    screen.blit(pion_image, (pion_x, pion_y))

    # Texte en haut de la fenêtre
    text_surface = chalk_font.render("By Damien & Gatien", True, WHITE)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 10))

    # Mettre à jour l'affichage
    pygame.display.update()

# Quitter pygame
pygame.quit()
