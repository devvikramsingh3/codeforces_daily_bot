import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        telegram_id INTEGER PRIMARY KEY,
        handle TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

def add_user(telegram_id, handle):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("REPLACE INTO users (telegram_id, handle) VALUES (?, ?)", (telegram_id, handle))
    conn.commit()
    conn.close()

def remove_user(telegram_id):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE telegram_id = ?", (telegram_id,))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT telegram_id, handle FROM users")
    users = c.fetchall()
    conn.close()
    return users
