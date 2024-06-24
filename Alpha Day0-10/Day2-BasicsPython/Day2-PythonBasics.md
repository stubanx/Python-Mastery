
# Day 2: Python Basics

## Data Types

Python supports various data types:

1. **Numbers**:
   - **Integers (`int`)**: Whole numbers (e.g., 42, -10).
   - **Floats (`float`)**: Decimal numbers (e.g., 3.14, -0.5).
   - **Long integers**: Large whole numbers (e.g., 1234567890L).
   - **Complex numbers**: Represented as `a + bj` (e.g., `3 + 4j`).

2. **Strings**:
   - Enclosed in single or double quotes (e.g., `"Hello, World!"`).
   - Manipulate strings using methods like `len()`, `upper()`, and `replace()`.

3. **Lists**, **Tuples**, and **Dictionaries**:
   - **Lists**: Ordered collections of items (mutable).
   - **Tuples**: Similar to lists but immutable (use parentheses).
   - **Dictionaries**: Key-value pairs (e.g., `{"name": "Alice", "age": 30}`).

4. **Boolean**:
   - Represents truth values: `True` or `False`.
   - Used for logical operations and control flow.

5. **None**:
   - Represents the absence of a value (similar to null in other languages).

## Basic Input and Output

- Use `input()` to get user input (stored as a string):
  ```python
  name = input("Enter your Full Name here: ")
  ```

- Print output using `print()` with optional formatting:
  ```python
  print("Hello!", name)
  ```

## Type Casting

In Python, you can convert data from one type to another using built-in functions:

1. **Integer (`int`) Conversion**:
   - Use `int()` to convert a value to an integer.
   - Example: `int("42")` returns `42`.

2. **Float (`float`) Conversion**:
   - Use `float()` to convert a value to a floating-point number.
   - Example: `float("3.14")` returns `3.14`.

3. **String (`str`) Conversion**:
   - Use `str()` to convert a value to a string.
   - Example: `str(42)` returns `"42"`.

## Operators

### Arithmetic Operators

- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division
- `//`: Floor division (returns an integer)
- `**`: Exponentiation
- `%`: Modulo (remainder after division)

### Comparison Operators

- `<`: Less than
- `>`: Greater than
- `<=`: Less than or equal to
- `>=`: Greater than or equal to
- `==`: Equal to
- `!=`: Not equal to

### Assignment Operators

- `=`: Assign a value
- `+=`: Add and assign
- `-=`: Subtract and assign (and others)

### Logical Operators

- `and`: Logical AND
- `or`: Logical OR
- `not`: Logical NOT

### Bitwise Operators

- `&`: Bitwise AND
- `|`: Bitwise OR
- `^`: Bitwise XOR
- `~`: Bitwise NOT (complement)
- `<<`: Left shift
- `>>`: Right shift

### Membership Operators

- `in`: Checks if an element exists in a sequence
- `not in`: Checks if an element does not exist in a sequence

### Identity Operators

- `is`: Checks if two objects are the same (have the same memory address)
- `is not`: Checks if two objects are not the same
