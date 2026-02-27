def generate_label(label_data):

    html_content = f"""
<!DOCTYPE html>
<html>
<head>
<title>FSSAI Nutrition Label</title>

<style>

body {{
    font-family: Arial, sans-serif;
    background-color:#f2f2f2;
}}

.container {{
    width:400px;
    margin:auto;
    padding:20px;
}}

.label {{
    border:4px solid black;
    background:white;
    padding:15px;
}}

.header {{
    text-align:center;
    border-bottom:3px solid black;
    padding-bottom:5px;
}}

.logo {{
    font-size:18px;
    font-weight:bold;
    color:green;
}}

.title {{
    font-size:22px;
    font-weight:bold;
}}

.serving {{
    margin-top:8px;
    font-size:14px;
}}

.row {{
    display:flex;
    justify-content:space-between;
    padding:6px 0;
    border-bottom:1px solid black;
}}

.bold {{
    font-weight:bold;
}}

.footer {{
    margin-top:10px;
    font-size:12px;
    text-align:center;
}}

</style>
</head>

<body>

<div class="container">

<div class="label">

<div class="header">
<div class="logo">FSSAI ✔</div>
<div class="title">NUTRITION INFORMATION</div>
<div class="serving">
Serving Size: {label_data['serving_size']}
</div>
</div>

<div class="row bold">
<span>Energy</span>
<span>{label_data['energy']} kcal</span>
</div>

<div class="row">
<span>Protein</span>
<span>{label_data['protein']} g</span>
</div>

<div class="row">
<span>Fat</span>
<span>{label_data['fat']} g</span>
</div>

<div class="row">
<span>Carbohydrates</span>
<span>{label_data['carbs']} g</span>
</div>

<div class="row">
<span>Sugar</span>
<span>{label_data['sugar']} g</span>
</div>

<div class="row">
<span>Sodium</span>
<span>{label_data['sodium']} mg</span>
</div>

<div class="footer">
Complies with FSSAI Nutritional Labelling Guidelines
</div>

</div>
</div>

</body>
</html>
"""

    with open("nutrition_label.html", "w") as file:
        file.write(html_content)

    print("✅ FSSAI Nutrition Label Generated Successfully!")