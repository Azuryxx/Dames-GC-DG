import pygame
from tkinter import Tk, Label, Entry, Button, messagebox
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game
from db import create_db, add_user, update_score, get_all_users, login_user

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MA-24 GATIEN & DAMIEN')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def login_window():
    """Affiche la fenêtre de login et gère la connexion/enregistrement."""

    def login():
        """Gère la connexion de l'utilisateur."""
        username = entry_username.get()
        password = entry_password.get()
        if username and password:
            if login_user(username, password):
                messagebox.showinfo("Succès", f"Bienvenue, {username} !")
                root.destroy()
                main_game(username)  # Lance le jeu avec le pseudo
            else:
                messagebox.showerror("Erreur", "Pseudo ou mot de passe incorrect.")
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

    def register():
        """Gère l'enregistrement d'un utilisateur."""
        username = entry_username.get()
        password = entry_password.get()
        if username and password:
            if add_user(username, password):
                messagebox.showinfo("Succès", "Utilisateur enregistré avec succès !")
            else:
                messagebox.showerror("Erreur", "Ce pseudo existe déjà.")
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

    def on_enter_pressed(event):
        """Gère l'événement quand la touche Enter est pressée dans le formulaire."""
        login()

    root = Tk()
    root.title("Page de login")
    root.geometry("300x300")
    root.configure(background='purple')


    Label(root, text="Pseudo:").pack(pady=5)
    entry_username = Entry(root)
    entry_username.pack(pady=5)

    Label(root, text="Mot de passe:").pack(pady=5)
    entry_password = Entry(root, show="*")
    entry_password.pack(pady=5)

    Button(root, text="Se connecter", command=login).pack(pady=10)
    Button(root, text="S'enregistrer", command=register).pack(pady=10)

    # Bind la touche Enter à la fonction 'on_enter_pressed' pour simuler un clic sur "Se connecter"
    root.bind('<Return>', on_enter_pressed)

    root.mainloop()


def main_game(username):
    """Lance le jeu principal après la connexion."""
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(f"{game.winner()} a gagné !")
            # Enregistre le score dans la base de données
            update_score(username, 100)  # Exemple : ajouter 100 points si le joueur gagne
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


if __name__ == "__main__":
    create_db()  # Crée la base de données si elle n'existe pas
    login_window()  # Affiche la fenêtre de login
