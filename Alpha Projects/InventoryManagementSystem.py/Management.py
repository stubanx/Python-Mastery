def display_inventory():
    print("Current Inventory:")
    for product, details in inventory.items():
        print(f"{product}: {details['quantity']} units (Price: ${details['price']:.2f} each)")

def calculate_total_value():
    total_value = sum(details["quantity"] * details["price"] for details in inventory.values())
    print(f"Total inventory value: ${total_value:.2f}")

    
# Initialize an empty inventory dictionary
inventory = {}
# Add sample products
inventory["apple"] = {"quantity": 100, "price": 0.5}
inventory["banana"] = {"quantity": 50, "price": 0.3}
inventory["orange"] = {"quantity": 80, "price": 0.4}

# Call the function to display inventory
display_inventory()

# Update apple quantity
inventory["apple"]["quantity"] += 50
print("Updated apple quantity:", inventory["apple"]["quantity"])


# Call the function to calculate total value
calculate_total_value()
