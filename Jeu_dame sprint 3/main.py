import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game

# Initialiser la fenêtre
WIN = pygame.display.set_mode((WIDTH + 150, HEIGHT + 150))  # Ajouter une bordure de 75 autour du plateau
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    offset = 75  # Décalage pour la bordure
    row = (y - offset) // SQUARE_SIZE
    col = (x - offset) // SQUARE_SIZE
    return row, col


def main():
    pygame.init()
    clock = pygame.time.Clock()
    game = Game(WIN)

    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()  # Mettre à jour l'affichage

    pygame.quit()


if __name__ == "__main__":
    main()
