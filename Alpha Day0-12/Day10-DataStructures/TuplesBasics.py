# Create a tuple called 'days_of_week'
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# Print the tuple
print("Days of the week:", days_of_week)

# Swap the first and last days
days_list = list(days_of_week)
days_list[0], days_list[-1] = days_list[-1], days_list[0]
updated_days_of_week = tuple(days_list)

# Print the updated tuple
print("Updated days of the week:", updated_days_of_week)

# Calculate the number of days
num_days = len(days_of_week)
print("Number of days:", num_days)

# Check if "Sunday" is present
sunday_present = "Sunday" in days_of_week
print("Is Sunday present?", sunday_present)



# Create a tuple with mixed data
mixed_data = ("John", 25, True, 3.14, "Python")

# Print the tuple
print("Mixed data tuple:", mixed_data)

