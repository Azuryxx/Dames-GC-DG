class Rules:
    def __init__(self, board):
        self.board = board
        self.current_player = 'rose'
        self.selected_pion = None
        self.selected_pion_index = None
        self.pions_rose = []  # Initialisez avec vos pions roses
        self.pions_jaune = []  # Initialisez avec vos pions jaunes

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Logique de sélection d'un pion
        if event.type == pygame.KEYDOWN:
            # Logique pour déplacer un pion sélectionné
            pass

    def is_valid_move(self, pion, new_pos):
        # Vérifie si le mouvement est valide
        pass

    def capture_pion(self, pion, captured_pion, pion_type):
        # Gère la capture de pions
        pass

    def move_pion_with_capture(self, pion, new_x, new_y, all_pions):
        # Gère les mouvements de pions avec capture
        pass