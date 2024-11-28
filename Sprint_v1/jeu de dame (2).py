import pygame

# Initialisation de pygame
pygame.init()

# Taille de la fenêtre et de chaque case
WIDTH = 500  # Largeur de la fenêtre
HEIGHT = 50  # Hauteur de la fenêtre
SQUARE_SIZE = WIDTH // 10  # Taille de chaque case (divisé en 10)

# Couleurs
WHITE = (255, 255, 255)
BLACK= ("BLACK")

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MA-24")

# Chargement de l'image du pion
pion_image = pygame.image.load("MA-24_pion (2).png")  # Charge l'image du pion
pion_image = pygame.transform.scale(pion_image, (SQUARE_SIZE, SQUARE_SIZE))  # Redimensionne l'image pour qu'elle tienne dans une case

# Position initiale du pion
pion_x = 0  # Le pion commence à la première case
pion_y = 0  # Le pion est aligné avec le haut de la fenêtre

# Fonction pour dessiner le damier
def draw_checkerboard():
    for col in range(10):  # Nous avons 10 cases sur la ligne
        if col % 2 == 0:
            color = WHITE  # Les cases impaires sont blanches
        else:
            color = BLACK  # Les cases paires sont grises
        pygame.draw.rect(screen, color, (col * SQUARE_SIZE, 0, SQUARE_SIZE, HEIGHT))

# Boucle principale du jeu
running = True
while running:
    # Vérifier les événements (comme quitter ou appuyer sur une touche)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si on clique sur le bouton de fermeture de la fenêtre
            running = False

        if event.type == pygame.KEYDOWN:  # Si une touche est enfoncée
            if event.key == pygame.K_RIGHT and pion_x + SQUARE_SIZE < WIDTH:  # Flèche droite
                pion_x += SQUARE_SIZE  # Déplacer le pion d'une case vers la droite
            elif event.key == pygame.K_LEFT and pion_x > 0:  # Flèche gauche
                pion_x -= SQUARE_SIZE  # Déplacer le pion d'une case vers la gauche

    # Remplir l'écran de blanc avant de dessiner
    screen.fill((255, 255, 255))

    # Dessiner le damier
    draw_checkerboard()

    # Dessiner le pion à sa position actuelle
    screen.blit(pion_image, (pion_x, pion_y))

    # Mettre à jour l'affichage
    pygame.display.update()

# Quitter pygame
pygame.quit()
