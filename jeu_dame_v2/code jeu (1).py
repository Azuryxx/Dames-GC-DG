import pygame

# Initialisation de pygame
pygame.init()

# Dimensions et paramètres
WIDTH, HEIGHT, OFFSET = 1000, 1000, 100
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

# Chargement des images
background_image = pygame.image.load("bois.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pion_image_rose = pygame.image.load("donut_rose.png")
pion_image_rose = pygame.transform.scale(pion_image_rose, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_jaune = pygame.image.load("donut_jaune.png")
pion_image_jaune = pygame.transform.scale(pion_image_jaune, (SQUARE_SIZE, SQUARE_SIZE))

# Classe pour les pions
class Piece:
    def __init__(self, x, y, color, image, is_king=False):
        self.x = x
        self.y = y
        self.color = color
        self.image = image
        self.is_king = is_king  # Attribut pour savoir si c'est une dame

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        if self.is_king:
            pygame.draw.circle(win, RED, (self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), 10)  # Marque la dame

    def move(self, dx, dy):
        self.x += dx * SQUARE_SIZE
        self.y += dy * SQUARE_SIZE

    def promote_to_king(self):
        self.is_king = True  # Promouvoir le pion en dame

# Création des pions pour chaque joueur
def create_pieces():
    pieces_rose, pieces_jaune = [], []
    for row in range(3):  # Trois premières rangées pour les pions roses
        for col in range(10):
            if (row + col) % 2 == 1:  # Cases noires uniquement
                x = OFFSET + col * SQUARE_SIZE
                y = OFFSET + row * SQUARE_SIZE
                pieces_rose.append(Piece(x, y, "rose", pion_image_rose))
    for row in range(7, 10):  # Trois dernières rangées pour les pions jaunes
        for col in range(10):
            if (row + col) % 2 == 1:  # Cases noires uniquement
                x = OFFSET + col * SQUARE_SIZE
                y = OFFSET + row * SQUARE_SIZE
                pieces_jaune.append(Piece(x, y, "jaune", pion_image_jaune))
    return pieces_rose, pieces_jaune

# Dessiner le damier
def draw_checkerboard():
    for row in range(10):
        for col in range(10):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (OFFSET + col * SQUARE_SIZE, OFFSET + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Dessiner la bordure
def draw_border():
    pygame.draw.rect(screen, WOOD_COLOR, (OFFSET - 5, OFFSET - 5, 10 * SQUARE_SIZE + 10, 10 * SQUARE_SIZE + 10), 5)

# Afficher le plateau et les pions
def draw_game(pions_rose, pions_jaune):
    screen.blit(background_image, (0, 0))
    draw_border()
    draw_checkerboard()

    for pion in pions_rose:
        pion.draw(screen)
    for pion in pions_jaune:
        pion.draw(screen)
    pygame.display.flip()

# Fonction pour déplacer un pion
def move_pion(pion, dx, dy):
    pion.move(dx, dy)

# Vérifier si un mouvement est valide
def can_move(pion, dx, dy, all_pions):
    new_x = pion.x + dx * SQUARE_SIZE
    new_y = pion.y + dy * SQUARE_SIZE

    # Vérifier si la nouvelle position est dans les limites du plateau
    if not (OFFSET <= new_x < OFFSET + 10 * SQUARE_SIZE and OFFSET <= new_y < OFFSET + 10 * SQUARE_SIZE):
        return False

    # Vérifier si la case est libre
    for piece in all_pions:
        if piece.x == new_x and piece.y == new_y:
            return False  # La case est occupée, mouvement invalide

    return True

# Fonction pour vérifier si un pion peut capturer
def can_capture(pion, dx, dy, all_pions):
    mid_x = pion.x + dx * SQUARE_SIZE // 2
    mid_y = pion.y + dy * SQUARE_SIZE // 2

    new_x = pion.x + dx * SQUARE_SIZE
    new_y = pion.y + dy * SQUARE_SIZE

    # Vérifier si le pion adverse est dans la case à sauter
    for piece in all_pions:
        if piece.x == mid_x and piece.y == mid_y and piece.color != pion.color:
            # Vérifier si la case après le saut est libre
            if can_move(pion, dx, dy, all_pions):
                return True
    return False

# Boucle principale du jeu
running = True
selected_pion_index = None
current_player = "rose"  # Le joueur "rose" commence
pions_rose, pions_jaune = create_pieces()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Vérifier si un pion a été sélectionné
            for idx, pion in enumerate(pions_rose):
                px, py = pion.x, pion.y
                if px <= x <= px + SQUARE_SIZE and py <= y <= py + SQUARE_SIZE:
                    selected_pion_index = idx
                    break
            if selected_pion_index is None:
                for idx, pion in enumerate(pions_jaune):
                    px, py = pion.x, pion.y
                    if px <= x <= px + SQUARE_SIZE and py <= y <= py + SQUARE_SIZE:
                        selected_pion_index = idx
                        break

        if event.type == pygame.KEYDOWN:
            if selected_pion_index is not None:
                # Déterminer le pion sélectionné
                if current_player == "rose":
                    pion = pions_rose[selected_pion_index]
                else:
                    pion = pions_jaune[selected_pion_index]

                # Détermine la direction du joueur actif
                ux, uy = (1, 1) if current_player == "rose" else (1, -1)

                if event.key == pygame.K_RIGHT:
                    if can_move(pion, ux, uy, pions_rose + pions_jaune):
                        move_pion(pion, ux, uy)
                        if (pion.color == "rose" and pion.y >= OFFSET + 8 * SQUARE_SIZE) or (pion.color == "jaune" and pion.y <= OFFSET + 1 * SQUARE_SIZE):
                            pion.promote_to_king()
                        current_player = "jaune" if current_player == "rose" else "rose"
                        selected_pion_index = None

                elif event.key == pygame.K_LEFT:
                    if can_move(pion, -ux, uy, pions_rose + pions_jaune):
                        move_pion(pion, -ux, uy)
                        if (pion.color == "rose" and pion.y >= OFFSET + 8 * SQUARE_SIZE) or (pion.color == "jaune" and pion.y <= OFFSET + 1 * SQUARE_SIZE):
                            pion.promote_to_king()
                        current_player = "jaune" if current_player == "rose" else "rose"
                        selected_pion_index = None

                # Gestion de la capture (saut)
                if event.key == pygame.K_UP:
                    if can_capture(pion, -1, -1, pions_rose + pions_jaune):
                        move_pion(pion, -1, -1)
                        current_player = "jaune" if current_player == "rose" else "rose"
                        selected_pion_index = None

                if event.key == pygame.K_DOWN:
                    if can_capture(pion, 1, 1, pions_rose + pions_jaune):
                        move_pion(pion, 1, 1)
                        current_player = "jaune" if current_player == "rose" else "rose"
                        selected_pion_index = None

    # Affichage du jeu
    draw_game(pions_rose, pions_jaune)

pygame.quit()
