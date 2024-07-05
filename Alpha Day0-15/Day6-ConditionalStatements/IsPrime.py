user_input = int(input("Enter a number: "))
ans = True  # Assume it's prime initially

if user_input < 2:
    ans = False
else:
    for i in range(2, int(user_input**0.5) + 1):
        if user_input % i == 0:
            ans = False
            break  # Exit the loop if a divisor is found

if ans:
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")
