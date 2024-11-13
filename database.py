import sqlite3

def init_db():
    conn = sqlite3.connect("reviews.db")
    cursor = conn.cursor()

    # Recréer la table avec la colonne user
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            rating TEXT,
            comment TEXT,
            user TEXT
        )
    ''')
    conn.commit()
    return conn, cursor

def insert_reviews(reviews):
    conn, cursor = init_db()
    cursor.executemany("INSERT INTO reviews (title, rating, comment, user) VALUES (?, ?, ?, ?)", reviews)
    conn.commit()
    conn.close()

def fetch_all_reviews():
    conn, cursor = init_db()
    cursor.execute("SELECT * FROM reviews")
    reviews = cursor.fetchall()
    conn.close()
    return reviews
