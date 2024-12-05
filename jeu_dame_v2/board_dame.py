import pygame


class Board:
    def __init__(self, screen, width, height, offset):
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.OFFSET = offset
        self.SQUARE_SIZE = (self.WIDTH - 2 * self.OFFSET) // 10

        # Couleurs
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.WOOD_COLOR = (139, 69, 19)
        self.SCORE_BOX_COLOR = (200, 200, 200)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)

        # Police et images
        self.chalk_font = pygame.font.Font("CoalhandLuke TRIAL.otf", 36)
        self.background_image = pygame.image.load("bois.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.WIDTH, self.HEIGHT))

        # Charger les images des pions
        self.pion_image_rose = pygame.image.load("donut_rose.png")
        self.pion_image_rose = pygame.transform.scale(self.pion_image_rose, (self.SQUARE_SIZE, self.SQUARE_SIZE))
        self.pion_image_rose_renne = pygame.image.load("renne_rose.png")
        self.pion_image_rose_renne = pygame.transform.scale(self.pion_image_rose_renne,
                                                            (self.SQUARE_SIZE, self.SQUARE_SIZE))
        self.pion_image_jaune = pygame.image.load("donut_jaune.png")
        self.pion_image_jaune = pygame.transform.scale(self.pion_image_jaune, (self.SQUARE_SIZE, self.SQUARE_SIZE))
        self.pion_image_jaune_renne = pygame.image.load("renne_jaune.png")
        self.pion_image_jaune_renne = pygame.transform.scale(self.pion_image_jaune_renne,
                                                             (self.SQUARE_SIZE, self.SQUARE_SIZE))

        # Scores
        self.score_rose = 0
        self.score_jaune = 0

    def draw_checkerboard(self):
        for row in range(10):
            for col in range(10):
                color = self.WHITE if (row + col) % 2 == 0 else self.BLACK
                pygame.draw.rect(self.screen, color,
                                 (self.OFFSET + col * self.SQUARE_SIZE, self.OFFSET + row * self.SQUARE_SIZE,
                                  self.SQUARE_SIZE, self.SQUARE_SIZE))

    def draw_border(self):
        pygame.draw.rect(self.screen, self.WOOD_COLOR,
                         (self.OFFSET - 5, self.OFFSET - 5, 10 * self.SQUARE_SIZE + 10, 10 * self.SQUARE_SIZE + 10), 5)

    def draw_score_boxes(self):
        box_width = self.SQUARE_SIZE * 4
        box_height = self.SQUARE_SIZE
        box_y = self.OFFSET + 10 * self.SQUARE_SIZE + 10

        pygame.draw.rect(self.screen, self.SCORE_BOX_COLOR, (self.OFFSET, box_y, box_width, box_height))
        text_red = self.chalk_font.render(f"Score Rouge: {self.score_rose}", True, self.RED)
        self.screen.blit(text_red, (self.OFFSET + box_width // 2 - text_red.get_width() // 2, box_y + box_height // 4))

        pygame.draw.rect(self.screen, self.SCORE_BOX_COLOR,
                         (self.WIDTH - self.OFFSET - box_width, box_y, box_width, box_height))
        text_blue = self.chalk_font.render(f"Score Bleu: {self.score_jaune}", True, self.BLUE)
        self.screen.blit(text_blue,
                         (self.WIDTH - self.OFFSET - box_width + box_width // 2 - text_blue.get_width() // 2,
                          box_y + box_height // 4))

    def draw_pions(self, pions_rose, pions_jaune):
        for pion in pions_rose:
            px, py = pion["pos"]
            if pion["promu"]:
                self.screen.blit(self.pion_image_rose_renne, (px, py))
            else:
                self.screen.blit(self.pion_image_rose, (px, py))

        for pion in pions_jaune:
            px, py = pion["pos"]
            if pion["promu"]:
                self.screen.blit(self.pion_image_jaune_renne, (px, py))
            else:
                self.screen.blit(self.pion_image_jaune, (px, py))

    def draw_game(self):
        self.screen.blit(self.background_image, (0, 0))
        self.draw_checkerboard()
        self.draw_border()
        self.draw_score_boxes()