from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# ---------------------------
# DATABASE INITIALIZATION
# ---------------------------

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredients (
        name TEXT PRIMARY KEY,
        calories REAL,
        protein REAL,
        carbs REAL,
        fat REAL,
        sugar REAL,
        sodium REAL
    )
    """)

    sample_data = [
        # Grains
        ("rice", 130, 2.7, 28, 0.3, 0.1, 1),
        ("wheat flour", 364, 10, 76, 1, 0.3, 2),
        ("maida", 364, 10, 76, 1, 0.3, 2),
        ("ragi", 336, 7.3, 72, 1.5, 0.6, 11),
        ("oats", 389, 17, 66, 7, 1, 2),

        # Pulses
        ("toor dal", 343, 22, 63, 1.5, 2.7, 15),
        ("moong dal", 347, 24, 63, 1.2, 6, 15),
        ("chana dal", 364, 21, 61, 5, 10, 24),
        ("rajma", 333, 24, 60, 1, 2.3, 12),
        ("chickpeas", 364, 19, 61, 6, 11, 24),

        # Dairy
        ("milk", 60, 3.2, 5, 3.3, 5, 44),
        ("curd", 98, 11, 3.4, 4.3, 3.4, 36),
        ("paneer", 265, 18, 1.2, 20, 1.2, 22),
        ("butter", 717, 0.9, 0.1, 81, 0.1, 11),
        ("ghee", 900, 0, 0, 100, 0, 0),

        # Vegetables
        ("potato", 77, 2, 17, 0.1, 0.8, 6),
        ("onion", 40, 1.1, 9.3, 0.1, 4.2, 4),
        ("tomato", 18, 0.9, 3.9, 0.2, 2.6, 5),
        ("carrot", 41, 0.9, 10, 0.2, 4.7, 69),
        ("spinach", 23, 2.9, 3.6, 0.4, 0.4, 79),

        # Oils
        ("sunflower oil", 884, 0, 0, 100, 0, 0),
        ("mustard oil", 884, 0, 0, 100, 0, 0),
        ("coconut oil", 892, 0, 0, 100, 0, 0),

        # Sweeteners
        ("sugar", 387, 0, 100, 0, 100, 1),
        ("jaggery", 383, 0.4, 98, 0.1, 97, 38),

        # Protein
        ("chicken", 239, 27, 0, 14, 0, 82),
        ("egg", 155, 13, 1.1, 11, 1.1, 124),

        # Nuts
        ("almonds", 579, 21, 22, 50, 4.4, 1),
        ("cashews", 553, 18, 30, 44, 6, 12),
        ("peanuts", 567, 26, 16, 49, 4, 18),
    ]

    cursor.executemany("""
    INSERT OR IGNORE INTO ingredients
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, sample_data)

    conn.commit()
    conn.close()

init_db()


# ---------------------------
# RECIPE PARSER
# ---------------------------

def parse_recipe(recipe):
    items = recipe.split(",")
    parsed = []

    for item in items:
        item = item.strip()
        if "g" in item:
            qty = float(item.split("g")[0])
            name = item.split("g")[1].strip().lower()
            parsed.append((name, qty))

    return parsed


# ---------------------------
# NUTRITION CALCULATION
# ---------------------------

def calculate_nutrition(parsed):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    totals = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0,
        "sugar": 0,
        "sodium": 0,
    }

    for name, qty in parsed:
        cursor.execute("SELECT * FROM ingredients WHERE name=?", (name,))
        row = cursor.fetchone()

        if row:
            _, cal, pro, carb, fat, sug, sod = row
            factor = qty / 100

            totals["calories"] += cal * factor
            totals["protein"] += pro * factor
            totals["carbs"] += carb * factor
            totals["fat"] += fat * factor
            totals["sugar"] += sug * factor
            totals["sodium"] += sod * factor
        else:
            print(f"Ingredient not found in DB: {name}")

    conn.close()
    return totals


# ---------------------------
# ROUTES
# ---------------------------

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        recipe_name = request.form["recipe_name"]
        recipe = request.form["recipe"]

        parsed = parse_recipe(recipe)
        totals = calculate_nutrition(parsed)

        return render_template(
            "label.html",
            recipe_name=recipe_name,
            totals=totals
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)