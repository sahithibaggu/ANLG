import re

class RecipeParserError(Exception):
    """Custom exception for recipe parsing errors."""
    pass


def parse_recipe(input_string):
    """
    Parses recipe input string and returns a dictionary:
    {
        "rice": 200,
        "milk": 100
    }

    Expected format:
    "200g rice, 100g milk"
    """

    if not input_string or not input_string.strip():
        raise RecipeParserError("Input cannot be empty.")

    recipe_dict = {}

    # Split ingredients by comma
    items = input_string.split(',')

    for item in items:
        item = item.strip()

        # Regex explanation:
        # (\d+)        → capture weight (one or more digits)
        # \s*          → optional spaces
        # g            → letter g (grams)
        # \s+          → at least one space
        # (.+)         → ingredient name
        pattern = r"^(\d+)\s*g\s+(.+)$"

        match = re.match(pattern, item, re.IGNORECASE)

        if not match:
            raise RecipeParserError(
                f"Invalid format: '{item}'. Use format like '200g rice'."
            )

        weight = int(match.group(1))
        ingredient = match.group(2).strip().lower()

        # Validate weight
        if weight <= 0:
            raise RecipeParserError(
                f"Weight must be greater than 0 for '{ingredient}'."
            )

        # Check duplicate ingredients
        if ingredient in recipe_dict:
            raise RecipeParserError(
                f"Duplicate ingredient detected: '{ingredient}'."
            )

        recipe_dict[ingredient] = weight

    return recipe_dict

if __name__ == "__main__":
    try:
        user_input = input("Enter recipe (e.g., 200g rice, 100g milk): ")
        parsed = parse_recipe(user_input)
        print("Parsed Recipe:", parsed)
    except RecipeParserError as e:
        print("Error:", e)
