import sqlite3
from contextlib import contextmanager

DB_PATH = "meal_planner.db"

# Context manager for database connections to ensure proper closing
@contextmanager
def get_db_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        yield conn
    finally:
        if conn:
            conn.close()

# Initialize database schema
def init_db():
    with get_db_connection() as conn:
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
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS meal_plans (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                user_id INTEGER NOT NULL,
                week_start TEXT NOT NULL,
                created_at TEXT NOT NULL,
                plan_json TEXT NOT NULL,
                FOREIGN KEY (user_id) references users (id)
            )
        """)

        conn.commit()

# Save user profile to the database
def save_user_profile(profile):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # Overwrite existing profile and create new profile
        try:
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
            return True
        except sqlite3.Error as e:
            conn.rollback()
            print(f"Database error: {e}")
            return False

# Retrieve user profile from database
def retrieve_user_profile():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

    # If rows are returned, convert to dictionary using column names
    if rows:
        columns = [description[0] for description in cursor.description]
        return {columns[i]: rows[0][i] for i in range(len(columns))}
    return None
