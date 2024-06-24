

user_string = input("Enter a string: ")
string = user_string.lower().replace(" ", "")  # Ignore spaces and case sensitivity
reversed_string = string[::-1]
if reversed_string == string:
    print(f"'{user_string}' is a palindrome.")
else:
    print(f"'{user_string}' is not a palindrome.")
