import sqlite3

DB_NAME = "ingredients.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        calories REAL,
        protein REAL,
        carbs REAL,
        fat REAL,
        sugar REAL,
        sodium REAL
    )
    """)

    conn.commit()
    conn.close()


def insert_ingredients():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    ingredients_data = [
        ("Rice", 130, 2.7, 28, 0.3, 0.1, 1),
        ("Milk", 42, 3.4, 5, 1, 5, 44),
        ("Sugar", 387, 0, 100, 0, 100, 1),
        ("Salt", 0, 0, 0, 0, 0, 38758),
        ("Egg", 155, 13, 1.1, 11, 1.1, 124),
        ("Apple", 52, 0.3, 14, 0.2, 10, 1),
        ("Banana", 89, 1.1, 23, 0.3, 12, 1),
    ]

    cursor.executemany("""
    INSERT OR IGNORE INTO ingredients
    (name, calories, protein, carbs, fat, sugar, sodium)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, ingredients_data)

    conn.commit()
    conn.close()


def get_ingredient(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name, calories, protein, carbs, fat, sugar, sodium
    FROM ingredients
    WHERE LOWER(name) = LOWER(?)
    """, (name,))

    result = cursor.fetchone()
    conn.close()

    if result:
        return {
            "name": result[0],
            "calories": result[1],
            "protein": result[2],
            "carbs": result[3],
            "fat": result[4],
            "sugar": result[5],
            "sodium": result[6]
        }
    return None


if __name__ == "__main__":
    create_database()
    insert_ingredients()
    print("Database ready.")