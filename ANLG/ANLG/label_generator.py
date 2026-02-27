def generate_label(fssai_data, serving_size):

    html_content = f"""
    <html>
    <head>
    <title>FSSAI Nutrition Label</title>
    <style>
    body {{ font-family: Arial; }}
    .box {{ border: 3px solid black; width: 350px; padding: 15px; }}
    .row {{ display: flex; justify-content: space-between; }}
    .bold {{ font-weight: bold; }}
    </style>
    </head>
    <body>
    <div class="box">
    <h2>NUTRITION INFORMATION</h2>
    <p>Serving Size: {serving_size} g</p>

    <div class="row bold"><span>Energy</span><span>{fssai_data['energy']} kcal</span></div>
    <div class="row"><span>Protein</span><span>{fssai_data['protein']} g</span></div>
    <div class="row"><span>Fat</span><span>{fssai_data['fat']} g</span></div>
    <div class="row"><span>Carbohydrates</span><span>{fssai_data['carbs']} g</span></div>
    <div class="row"><span>Sugar</span><span>{fssai_data['sugar']} g</span></div>
    <div class="row"><span>Sodium</span><span>{fssai_data['sodium']} mg</span></div>

    </div>
    </body>
    </html>
    """

    with open("nutrition_label.html", "w") as file:
        file.write(html_content)

    print("✅ Nutrition label generated: nutrition_label.html")