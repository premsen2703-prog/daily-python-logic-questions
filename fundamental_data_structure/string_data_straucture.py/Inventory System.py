# 1. Nested Structure: A dictionary of products with their stock and tags
inventory = {
    "PROD001": {"name": "Laptop", "stock": 10, "tags": {"electronics", "work"}},
    "PROD002": {"name": "Coffee Mug", "stock": 0, "tags": {"kitchen", "home"}},
    "PROD003": {"name": "Wireless Mouse", "stock": 5, "tags": {"electronics", "accessories"}},
}

# 2. TODO: Write a LIST COMPREHENSION to get the names of products that are OUT OF STOCK (stock == 0)
# Hint: loop over inventory.values()
out_of_stock = [item["name"] for item in inventory.values() if item["stock"] == 0]
print("Out of Stock:", out_of_stock)  # Expected: ['Coffee Mug']


# 3. TODO: Write a SET COMPREHENSION to extract all unique tags across ALL products
# Hint: You will need a nested loop inside the comprehension or handle the set of tags
all_tags = {tag for item in inventory.values() for tag in item["tags"]}
print("All Unique Tags:", all_tags) 
# Expected: {'electronics', 'work', 'kitchen', 'home', 'accessories'} (order may vary)


# 4. Tricky Mutability Check: Restocking an item safely
def restock_item(item_id, quantity):
    # TODO: Safely update the stock value inside our nested inventory dictionary
    if item_id in inventory:
        inventory[item_id]["stock"] += quantity

restock_item("PROD001", 5)
print("Updated Laptop Stock:", inventory["PROD001"]["stock"])  # Expected: 15
