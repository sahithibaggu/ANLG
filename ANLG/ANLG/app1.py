from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_data(name):
    conn = sqlite3.connect("nutrition.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM ingredients WHERE name=?", (name,))
    row = cur.fetchone()
    conn.close()
    return row

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    ingredients = request.form.getlist("ingredient")
    weights = request.form.getlist("weight")

    total = {
        "calories": 0,
        "protein": 0,
        "fat": 0,
        "carbs": 0,
        "sugar": 0,
        "sodium": 0
    }

    total_weight = sum([float(w) for w in weights])

    for ing, wt in zip(ingredients, weights):
        data = get_data(ing.lower())
        if not data:
            return f"{ing} not found in database"

        _, cal, pro, fat, carb, sug, sod = data
        factor = float(wt) / 100

        total["calories"] += cal * factor
        total["protein"] += pro * factor
        total["fat"] += fat * factor
        total["carbs"] += carb * factor
        total["sugar"] += sug * factor
        total["sodium"] += sod * factor

    # Convert to per 100g
    for k in total:
        total[k] = round((total[k] / total_weight) * 100, 2)

    return render_template("result.html", n=total)