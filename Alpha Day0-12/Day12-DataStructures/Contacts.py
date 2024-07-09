# Create a dictionary called 'contact_book'
contact_book = {
    "Johhny": {"phone": "123-456-7890", "email": "john@example.com"},
    "kodesmiths": {"phone": "987-654-3210", "email": "koders@example.com"},
    "Harry Potter": {"phone": "555-123-4567", "email": "potter@dobby.com"}
}

# Print the dictionary
print("Contact book:", contact_book)

# Add a new contact for "Eva Brown"
contact_book["Eva Brown"] = {"phone": "555-987-6543", "email": "eva@example.com"}

# Print the updated dictionary
print("Updated contact book:", contact_book)

# Retrieve the phone number for "Harry Potter"
harry_phone = contact_book["Harry Potter"]["phone"]
print("Harry Potter's phone number:", harry_phone)

# Update the email address for "Johhny"
contact_book["Johhny"]["email"] = "dk.smith@example.com"

# Print the updated dictionary
print("Updated contact book after email update:", contact_book)
