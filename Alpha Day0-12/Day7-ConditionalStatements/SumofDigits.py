# Sum of Digits
number = int(input("Enter a positive integer: "))
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10
print(f"Sum of digits: {sum_of_digits}")
