# Input Validation
user_response = input("Enter 'yes' or 'no': ").lower()
while user_response not in ["yes", "no"]:
    print("Invalid input. Please try again.")
    user_response = input("Enter 'yes' or 'no': ").lower()
print(f"You entered: {user_response}")
