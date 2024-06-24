
## Python `while` Loops Assignment

### Part 1: Countdown

1. **Countdown Timer**:
    - Write a program that counts down from a user-specified positive integer (e.g., 10) to 1.
    - Use a `while` loop to print each countdown value.
    - After reaching 1, print "Blastoff!"

### Part 2: User Input Validation

2. **Input Validation**:
    - Create a function called `get_yes_or_no`:
        - Continuously prompt the user to enter either "yes" or "no" (case-insensitive).
        - Use a `while` loop to validate the input.
        - Return the validated input.
    - Example usage:
        ```python
        user_response = get_yes_or_no()
        print(f"You entered: {user_response}")
        ```

### Part 3: Sum of Digits

3. **Sum of Digits**:
    - Write a program that calculates the sum of the digits of a positive integer entered by the user.
    - Use a `while` loop to repeatedly extract digits and update the sum.
    - Example:
        ```
        Enter a positive integer: 12345
        Sum of digits: 15
        ```

### Bonus Challenge:

4. **Collatz Conjecture**:
    - Implement the Collatz sequence for a given positive integer:
        - If the number is even, divide it by 2.
        - If the number is odd, multiply it by 3 and add 1.
        - Repeat until the number becomes 1.
    - Print the entire sequence.
    - Example:
        ```
        Enter a positive integer: 6
        6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
        ```
