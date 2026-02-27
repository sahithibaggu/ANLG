import re

# -------- Recipe Parser --------
def parse_recipe(recipe_text):

    pattern = r"(\d+)\s*g\s*(\w+)"
    matches = re.findall(pattern, recipe_text.lower())

    recipe = {}

    for weight, ingredient in matches:
        recipe[ingredient] = float(weight)

    return recipe


# -------- Dummy Nutrition Calculator --------
def calculate_nutrition(recipe):

    # sample values (demo purpose)
    return {
        "energy": 350,
        "protein": 6,
        "fat": 4,
        "carbs": 60,
        "sugar": 25,
        "sodium": 45
    }


# -------- FSSAI Rules --------
def apply_fssai_rules(data):

    data["serving_size"] = "100g"

    for k in data:
        if isinstance(data[k], float) or isinstance(data[k], int):
            data[k] = round(data[k],2)

    return data


# -------- Label Generator --------
def generate_label(label_data):

    html = f"""
    <html>
    <body style="font-family:Arial;
                 border:2px solid black;
                 width:300px;
                 padding:15px">

    <h2>NUTRITION INFORMATION</h2>

    Serving Size: {label_data['serving_size']}<br><hr>

    Energy: {label_data['energy']} kcal<br>
    Protein: {label_data['protein']} g<br>
    Fat: {label_data['fat']} g<br>
    Carbohydrates: {label_data['carbs']} g<br>
    Sugar: {label_data['sugar']} g<br>
    Sodium: {label_data['sodium']} mg<br>

    </body>
    </html>
    """

    with open("nutrition_label.html","w") as f:
        f.write(html)

    print("✅ Label Generated")


# -------- MAIN APP --------
print("Enter Recipe Example: 200g rice 100g milk")

recipe_input = input("Enter Recipe: ")

recipe = parse_recipe(recipe_input)

nutrition = calculate_nutrition(recipe)

label = apply_fssai_rules(nutrition)

generate_label(label)