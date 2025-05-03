import sqlite3

DB_PATH = "meal_planner.db"

conn = sqlite3.connect(DB_PATH)

def init_db():
    return conn
    
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