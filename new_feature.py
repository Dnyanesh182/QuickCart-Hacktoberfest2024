# Description: This file adds a new feature to the QuickCart Shopping List Application.

import json

# Sample function to add a new item to the shopping list JSON file
def add_item(item_name, category, amount, price):
    """Add a new item to the shopping list with specified attributes."""
    try:
        with open("shopping_list.json", "r") as file:
            shopping_list = json.load(file)
        
        # Add the new item
        shopping_list.append({
            "name": item_name,
            "category": category,
            "amount": amount,
            "price": price
        })
        
        # Save changes back to the JSON file
        with open("shopping_list.json", "w") as file:
            json.dump(shopping_list, file, indent=4)
        
        print(f"Item '{item_name}' added to the shopping list.")

    except Exception as e:
        print(f"Error adding item: {e}")

# Example usage
if __name__ == "__main__":
    add_item("Bananas", "Grocery", 6, 0.5)
