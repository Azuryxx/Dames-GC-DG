import sqlite3

DB_NAME = "users.db"

def create_db():
    """Crée la base de données et la table users si elle n'existe pas."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        score INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()

def add_user(username, password):
    """Ajoute un utilisateur dans la base de données."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def login_user(username, password):
    """Vérifie si l'utilisateur existe et le mot de passe est correct."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def update_score(username, score):
    """Met à jour le score d'un utilisateur."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET score = score + ? WHERE username = ?", (score, username))
    conn.commit()
    conn.close()

def get_all_users():
    """Retourne tous les utilisateurs et leurs scores."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT username, score FROM users ORDER BY score DESC")
    users = cursor.fetchall()
    conn.close()
    return users
