# Create an empty list called 'fruits'
fruits = []

# Add fruits to the list
fruits.extend(["apple", "banana", "cherry", "grape"])

# Print the list
print("Fruits list:", fruits)

# Extract the second and third fruits (index 1 and 2)
sliced_fruits = fruits[1:3]

# Print the extracted sublist
print("Sliced fruits:", sliced_fruits)

# Create another list called 'numbers'
numbers = [10, 20, 30, 40]

# Concatenate 'fruits' with 'numbers'
combined_list = fruits + numbers

# Print the combined list
print("Combined list:", combined_list)






# Generate a list of squares for numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]

# Print the list of squares
print("List of squares:", squares)

