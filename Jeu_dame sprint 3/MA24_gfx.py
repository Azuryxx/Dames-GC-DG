import pygame

# Initialiser Pygame (si nécessaire pour les ressources comme les polices)
pygame.init()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WOOD_COLOR = (139, 69, 19)
SCORE_BOX_COLOR = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Constantes de taille
OFFSET = 100
SQUARE_SIZE = 80
WIDTH = 1000
HEIGHT = 1000

# Chargement des ressources
chalk_font = pygame.font.Font("CoalhandLuke TRIAL.otf", 36)
background_image = pygame.image.load("bois.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pion_image = pygame.image.load("pion_donut_rose.png")
pion_image = pygame.transform.scale(pion_image, (SQUARE_SIZE, SQUARE_SIZE))


def draw_checkerboard(screen):
    """Dessine le damier 10x10."""
    for row in range(10):
        for col in range(10):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(
                screen,
                color,
                (OFFSET + col * SQUARE_SIZE, OFFSET + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )


def draw_border(screen):
    """Dessine la bordure autour du damier."""
    pygame.draw.rect(
        screen,
        WOOD_COLOR,
        (OFFSET - 5, OFFSET - 5, 10 * SQUARE_SIZE + 10, 10 * SQUARE_SIZE + 10),
        5,
    )


def draw_score_boxes(screen):
    """Dessine les cases de score avec des textes."""
    box_width = SQUARE_SIZE * 4
    box_height = SQUARE_SIZE
    box_y = OFFSET + 10 * SQUARE_SIZE + 10

    # Case pour le score du joueur rouge
    pygame.draw.rect(screen, SCORE_BOX_COLOR, (OFFSET, box_y, box_width, box_height))
    text_red = chalk_font.render("Score Rouge: 0", True, RED)
    screen.blit(
        text_red,
        (OFFSET + box_width // 2 - text_red.get_width() // 2, box_y + box_height // 4),
    )

    # Case pour le score du joueur bleu
    pygame.draw.rect(screen, SCORE_BOX_COLOR, (WIDTH - OFFSET - box_width, box_y, box_width, box_height))
    text_blue = chalk_font.render("Score Bleu: 0", True, BLUE)
    screen.blit(
        text_blue,
        (
            WIDTH - OFFSET - box_width + box_width // 2 - text_blue.get_width() // 2,
            box_y + box_height // 4,
        ),
    )


def draw_header_text(screen, text):
    """Affiche un texte en haut de l'écran."""
    text_surface = chalk_font.render(text, True, WHITE)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 10))


def draw_background(screen):
    """Affiche l'image d'arrière-plan."""
    screen.blit(background_image, (0, 0))


def draw_pion(screen, x, y):
    """Dessine le pion à une position donnée."""
    screen.blit(pion_image, (x, y))


def can_move(new_x, new_y):
    """Vérifie si le pion peut être déplacé à une position donnée."""
    min_x = OFFSET
    max_x = OFFSET + 9 * SQUARE_SIZE
    min_y = OFFSET
    max_y = OFFSET + 9 * SQUARE_SIZE  # Correction ici
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y

