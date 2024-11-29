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
pion_image_jaune = pygame.image.load("donut_jaune.png")
pion_image_jaune = pygame.transform.scale(pion_image_jaune, (SQUARE_SIZE, SQUARE_SIZE))
pion_image_rose_renne = pygame.image.load("renne_rose.png")
pion_image_rose_renne = pygame.transform.scale(pion_image_rose_renne, (SQUARE_SIZE, SQUARE_SIZE))

# Positions initiales des pions (x, y, couronne)
pions_rose = [(OFFSET + i * SQUARE_SIZE, OFFSET, False) for i in range(1, 10, 2)] + \
             [(OFFSET + i * SQUARE_SIZE, OFFSET + SQUARE_SIZE, False) for i in range(0, 10, 2)]
pions_jaune = [(OFFSET + i * SQUARE_SIZE, OFFSET + 8 * SQUARE_SIZE, False) for i in range(0, 10, 2)] + \
              [(OFFSET + i * SQUARE_SIZE, OFFSET + 9 * SQUARE_SIZE, False) for i in range(1, 10, 2)]

running = True
current_player = "rose"
selected_pion_index = None


# Fonction pour dessiner le damier
def draw_checkerboard():
    for row in range(10):
        for col in range(10):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (OFFSET + col * SQUARE_SIZE, OFFSET + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


# Fonction pour dessiner la bordure
def draw_border():
    pygame.draw.rect(screen, WOOD_COLOR, (OFFSET - 5, OFFSET - 5, 10 * SQUARE_SIZE + 10, 10 * SQUARE_SIZE + 10), 5)


# Fonction pour vérifier si un mouvement est possible
def can_move(new_x, new_y, all_pions):
    if not (OFFSET <= new_x < OFFSET + 10 * SQUARE_SIZE and OFFSET <= new_y < OFFSET + 10 * SQUARE_SIZE):
        return False
    return all((px, py) != (new_x, new_y) for px, py, _ in all_pions)




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
    for x, y, _ in pions_jaune:
        screen.blit(pion_image_jaune, (x, y))

    pygame.display.update()


# Boucle principale
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if current_player == "rose":
                for idx, (px, py, _) in enumerate(pions_rose):
                    if px <= x <= px + SQUARE_SIZE and py <= y <= py + SQUARE_SIZE:
                        selected_pion_index = idx
                        break

        if event.type == pygame.KEYDOWN and selected_pion_index is not None:
            if current_player == "rose":
                pion = pions_rose[selected_pion_index]
            else:
                pion = pions_jaune[selected_pion_index]

            px, py, couronne = pion
            new_x, new_y = px, py

            # Déplacements
            if event.key == pygame.K_RIGHT:
                new_x += SQUARE_SIZE
                new_y -= SQUARE_SIZE
            elif event.key == pygame.K_LEFT:
                new_x -= SQUARE_SIZE
                new_y += SQUARE_SIZE
            elif event.key == pygame.K_DOWN:
                new_x += SQUARE_SIZE
                new_y += SQUARE_SIZE
            elif event.key == pygame.K_UP:
                new_x -= SQUARE_SIZE
                new_y -= SQUARE_SIZE

            # Déplacement valide
            if can_move(new_x, new_y, pions_rose + pions_jaune):
                if current_player == "rose":
                    if new_y == OFFSET + 9 * SQUARE_SIZE:
                        couronne = True
                    pions_rose[selected_pion_index] = (new_x, new_y, couronne)

                selected_pion_index = None  # Réinitialiser le pion sélectionné


    draw_game()

pygame.quit()
