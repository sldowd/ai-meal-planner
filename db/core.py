import sqlite3

DB_PATH = "meal_planner.db"

conn = sqlite3.connect(DB_PATH)

def init_db():
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            skill_level TEXT,
            diet_tags TEXT,
            allergies TEXT,
            time_per_meal INTEGER,
            servings INTEGER,
            budget REAL
        )
        """)

    conn.commit()
    conn.close()


def save_user_profile(profile):
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users")  # overwrite for MVP

    cursor.execute("""
        INSERT INTO users (name, skill_level, diet_tags, allergies, time_per_meal, servings, budget)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        profile["name"],
        profile["skill_level"],
        profile["diet_tags"],
        profile["allergies"],
        profile["time_per_meal"],
        profile["servings"],
        profile["budget"]
    ))

    conn.commit()
    conn.close()
    

def retrieve_user_profile():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()