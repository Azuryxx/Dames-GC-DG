import pygame
import MA24_gfx as gfx  # Importation du module graphique

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH = 1000
HEIGHT = 1000

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ma-24-DG-GC")

# Position initiale du pion
pion_x = gfx.OFFSET + 80
pion_y = gfx.OFFSET

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Définir la nouvelle position potentielle
            new_x, new_y = pion_x, pion_y

            if event.key == pygame.K_RIGHT:
                new_x += gfx.SQUARE_SIZE
                new_y += gfx.SQUARE_SIZE
            elif event.key == pygame.K_LEFT:
                new_x -= gfx.SQUARE_SIZE
                new_y -= gfx.SQUARE_SIZE
            elif event.key == pygame.K_DOWN:
                new_y += gfx.SQUARE_SIZE
                new_x -= gfx.SQUARE_SIZE
            elif event.key == pygame.K_UP:
                new_y -= gfx.SQUARE_SIZE
                new_x += gfx.SQUARE_SIZE

            # Vérifier si le mouvement est autorisé
            if gfx.can_move(new_x, new_y):
                pion_x, pion_y = new_x, new_y
            else:
                print("Erreur : Mouvement impossible, vous êtes au bord du damier !")

    # Afficher l'arrière-plan
    gfx.draw_background(screen)

    # Dessiner le damier et la bordure
    gfx.draw_border(screen)
    gfx.draw_checkerboard(screen)

    # Dessiner les cases de score
    gfx.draw_score_boxes(screen)

    # Dessiner le pion
    gfx.draw_pion(screen, pion_x, pion_y)

    # Dessiner le texte en haut
    gfx.draw_header_text(screen, "By Damien & Gatien")

    # Mettre à jour l'affichage
    pygame.display.update()

# Quitter Pygame
pygame.quit()
