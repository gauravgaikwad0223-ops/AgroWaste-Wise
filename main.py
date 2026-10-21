import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "waste_data.json"


def load_waste_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Waste dataset could not be loaded.")
        return {}


def display_categories(data):
    print("\nAvailable Agricultural Waste Categories:")

    for category in data:
        print(f"- {category}")


def get_recommendations(data, category, quantity):
    category_data = data.get(category)

    if not category_data:
        return None

    return {
        "quantity": quantity,
        "methods": category_data["methods"],
        "description": category_data["description"]
    }


def main():
    data = load_waste_data()

    if not data:
        return

    print("=" * 40)
    print("       AGROWASTE WISE")
    print(" Agricultural Waste Management")
    print("=" * 40)

    display_categories(data)

    category = input(
        "\nEnter waste category: "
    ).strip().lower()

    try:
        quantity = float(input("Enter waste quantity in kg: "))

        if quantity <= 0:
            print("Please enter a quantity greater than zero.")
            return

    except ValueError:
        print("Please enter a valid numeric quantity.")
        return

    result = get_recommendations(data, category, quantity)

    if result is None:
        print("Category not found. Please check the category name.")
        return

    print("\n--- RECOMMENDATION ---")
    print(f"Category: {category.title()}")
    print(f"Quantity: {result['quantity']} kg")
    print(f"Description: {result['description']}")
    print("Suggested reuse methods:")

    for method in result["methods"]:
        print(f"- {method}")

    print("\nNote: Suggestions are general examples.")
    print("Actual suitability depends on waste quality and conditions.")


if __name__ == "__main__":
    main()