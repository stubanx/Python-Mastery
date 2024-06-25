# Create a set called 'kitchen_utensils'
kitchen_utensils = {"plates", "bowls", "glasses", "cooking utensils", "tableware"}

# Print the set
print("Kitchen utensils set:", kitchen_utensils)

# Add more utensils to the set
kitchen_utensils.update({"spatula", "ladle", "whisk"})

# Remove any duplicates (if accidentally added)
# Note: Sets automatically handle duplicates, so no explicit removal needed

# Print the updated set
print("Updated kitchen utensils set:", kitchen_utensils)

# Check if "spatula" is present
spatula_present = "spatula" in kitchen_utensils
print("Is 'spatula' present?", spatula_present)

# Check if "fork" is present
fork_present = "fork" in kitchen_utensils
print("Is 'fork' present?", fork_present)
