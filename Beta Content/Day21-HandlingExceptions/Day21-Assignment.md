
# Exception Handling Assignment

## Task 1: Divide by Zero

1. Write a function called `safe_divide(a, b)` that takes two arguments, `a` and `b`.
2. Inside the function, use a `try` block to perform the division `a / b`.
3. If `b` is zero, catch the `ZeroDivisionError` and print an error message.
4. Otherwise, return the result of the division.

Example:
```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

# Test cases
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(8, 0))   # Output: Error: Cannot divide by zero!
```

## Task 2: File Reading

1. Create a text file named `data.txt` with some random content.
2. Write a function called `read_file(filename)` that reads the content of the file.
3. Use a `try` block to open the file and read its content.
4. If the file does not exist, catch the `FileNotFoundError` and print an error message.

Example:
```python
def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")

# Test case
read_file("data.txt")
```

## Task 3: Custom Exception

1. Create a custom exception class called `NegativeValueError`.
2. Write a function called `check_positive(num)` that takes an integer `num`.
3. If `num` is negative, raise a `NegativeValueError` with an appropriate message.
4. Otherwise, print a success message.

Example:
```python
class NegativeValueError(Exception):
    pass

def check_positive(num):
    try:
        if num < 0:
            raise NegativeValueError("Negative values are not allowed.")
        else:
            print("Value is positive!")
    except NegativeValueError as e:
        print(f"Error: {e}")

# Test cases
check_positive(10)   # Output: Value is positive!
check_positive(-5)   # Output: Error: Negative values are not allowed.
```

---

Feel free to customize or expand upon these tasks to suit your students' needs. Happy coding! 🚀🐍