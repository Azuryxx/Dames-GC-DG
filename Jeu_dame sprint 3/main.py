import pygame
from checkers.game import Game

# Initialisation de Pygame
pygame.init()

# Définir la fenêtre
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Dames")

# Fonction pour obtenir les coordonnées d'une case à partir de la souris
def get_row_col_from_mouse(pos):
    x, y = pos
    offset_x = (WIDTH - 10 * 80) // 2  # Damier centré
    offset_y = (HEIGHT - 10 * 80) // 2
    row = (y - offset_y) // 80
    col = (x - offset_x) // 80
    return row, col

# Fonction principale pour gérer la boucle du jeu
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

# Lancer le jeu
main()
