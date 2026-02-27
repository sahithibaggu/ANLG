# fssai_rules.py

def format_for_fssai(nutrition_totals, total_weight):
    """
    nutrition_totals: output from calculate_totals()
    total_weight: total recipe weight in grams
    """

    per_100g = {}
    per_serving = {}

    for key, value in nutrition_totals.items():
        per_100g[key] = round((value / total_weight) * 100, 2)
        per_serving[key] = round(value, 2)

    fssai_format = {
        "per_100g": {
            "Energy (kcal)": per_100g["energy"],
            "Protein (g)": per_100g["protein"],
            "Fat (g)": per_100g["fat"],
            "Carbohydrates (g)": per_100g["carbs"],
            "Sugar (g)": per_100g["sugar"],
            "Sodium (mg)": per_100g["sodium"]
        },
        "per_serving": {
            "Energy (kcal)": per_serving["energy"],
            "Protein (g)": per_serving["protein"],
            "Fat (g)": per_serving["fat"],
            "Carbohydrates (g)": per_serving["carbs"],
            "Sugar (g)": per_serving["sugar"],
            "Sodium (mg)": per_serving["sodium"]
        }
    }

    return fssai_format