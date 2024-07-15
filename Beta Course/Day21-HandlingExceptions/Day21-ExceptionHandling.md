# Day 21
### What is an Exception?
An exception is an unexpected situation or error that occurs during the execution of a program. It's like a red flag signaling that something went wrong. In Python, exceptions are represented by objects of specific types. For example:
- If you try to divide a number by zero, you'll encounter a `ZeroDivisionError`.
- When a file you're trying to read doesn't exist, you'll get a `FileNotFoundError`.

### Try and Except Blocks
Python's `try` and `except` blocks allow you to handle exceptions gracefully. Here's how they work:

1. **Try Block**: You wrap a piece of code in a `try` block. Python attempts to execute this code.
2. **Except Block**: If an exception occurs within the `try` block, Python jumps to the corresponding `except` block. You can specify which type of exception to catch.

### Real-Life Example: Division by Zero
Suppose you're building a calculator app, and a user enters `10 / 0`. Without exception handling, your program would crash. But with it, you can do this:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
```

### Handling Multiple Exceptions
You can catch different exceptions in separate `except` blocks. For instance:

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
except ValueError:
    print("Please enter a valid number.")
```

### The `finally` Block
Sometimes you want to execute code regardless of whether an exception occurred. Use the `finally` block:

```python
try:
    # Some risky operation
except SomeException:
    # Handle the exception
finally:
    # This code runs no matter what
```

### Custom Exceptions
You can create your own exception classes for specific scenarios. For example, if your app processes financial transactions, you might define a custom `InsufficientFundsError`.

### Conclusion
Exception handling makes your Python programs robust and user-friendly. By mastering it, you'll confidently tackle unexpected errors and keep your code running smoothly! 🚀
