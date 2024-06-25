# Day 8: Functions


## Functions in Python

1. **What is a Function?**
    - A **function** is a reusable block of code that performs a specific task.
    - Functions allow you to organize your code, make it more modular, and avoid repetition.
    - You can think of functions as mini-programs within your larger program.

2. **Defining a Function**:
    - To define a function, use the `def` keyword followed by the function name and parentheses.
    - Inside the parentheses, you can specify parameters (inputs) that the function accepts.
    - Example:
        ```python
        def greet(name):
            print(f"Hello, {name}!")

        greet("Alice")  # Calling the function
        ```

3. **Function Call**:
    - To use a function, call it by its name followed by parentheses.
    - You can pass arguments (values) to the function.
    - Example:
        ```python
        def add(a, b):
            return a + b

        result = add(3, 5)
        print("Sum:", result)
        ```

4. **Return Statement**:
    - Functions can return values using the `return` statement.
    - The returned value can be assigned to a variable or used directly.
    - Example:
        ```python
        def multiply(x, y):
            return x * y

        product = multiply(4, 7)
        print("Product:", product)
        ```

5. **Default Arguments**:
    - You can provide default values for function parameters.
    - If an argument is not explicitly passed, the default value is used.
    - Example:
        ```python
        def greet(name="Guest"):
            print(f"Hello, {name}!")

        greet()  # Using the default value
        greet("Bob")  # Passing an argument
        ```

6. **Scope**:
    - Variables defined inside a function have local scope (they are only accessible within the function).
    - Variables defined outside a function have global scope (they can be accessed anywhere in the program).

7. **Recursion**:
    - Recursion is a technique where a function calls itself.
    - Example (factorial calculation):
        ```python
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)

        print(factorial(5))  # Output: 120 (5! = 5 * 4 * 3 * 2 * 1)
        ```

8. **Best Practices**:
    - Use meaningful function names.
    - Keep functions short and focused (single responsibility principle).
    - Document your functions using docstrings.

Remember that functions are essential for writing clean, maintainable code. Feel free to experiment and create your own functions! 😊🚀🐍