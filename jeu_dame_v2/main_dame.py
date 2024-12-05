HEIGHT = 1000
OFFSET = 100

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Dames")

# Initialisation des composants du jeu
board = Board(screen, WIDTH, HEIGHT, OFFSET)
rules = Rules(board)

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Gérer les interactions utilisateur
        rules.handle_event(event)

    # Mise à jour du plateau
    board.draw_game()
    pygame.display.update()

pygame.quit()

