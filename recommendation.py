import pandas as pd
import numpy as np
from collections import Counter
from bs4 import BeautifulSoup

# Function to parse HTML files and extract data
def extract_data_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        items = [item.text.strip() for item in soup.find_all('li')]
    return items

# Extract menu items, cart orders, and reservations
menu_items = extract_data_from_html('menu.html')
cart_orders = extract_data_from_html('cart.html')
reservations = extract_data_from_html('book.html')

# Count occurrences of each ordered dish
order_counts = Counter(cart_orders)

# Recommend only frequently ordered items
def recommend_repeated_dishes(order_counts, min_occurrences=2):
    """Recommend dishes that have been ordered multiple times."""
    repeated_dishes = [dish for dish, count in order_counts.items() if count >= min_occurrences]
    return repeated_dishes

# Get repeated dish recommendations
recommended_meals = recommend_repeated_dishes(order_counts)
print(f"Recommended frequently ordered dishes: {recommended_meals}")