def calculate_totals(recipe_dict):
    totals = {
        "energy": 0.0,
        "protein": 0.0,
        "fat": 0.0,
        "carbs": 0.0,
        "sugar": 0.0,
        "sodium": 0.0
    }

    total_weight = 0

    for ingredient in recipe_dict.values():
        weight = ingredient["weight"]
        nutrition = ingredient["nutrition_per_100g"]

        total_weight += weight

        totals["energy"] += (nutrition["calories"] * weight) / 100
        totals["protein"] += (nutrition["protein"] * weight) / 100
        totals["fat"] += (nutrition["fat"] * weight) / 100
        totals["carbs"] += (nutrition["carbs"] * weight) / 100
        totals["sugar"] += (nutrition["sugar"] * weight) / 100
        totals["sodium"] += (nutrition["sodium"] * weight) / 100

    for key in totals:
        totals[key] = round(totals[key], 2)

    return totals, total_weight