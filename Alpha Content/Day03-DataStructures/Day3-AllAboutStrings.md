# Day 3: All About Strings

## String Basics

Strings in Python can be enclosed in single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`). Here are some examples:

- Single-quoted string: `'Hello, Python!'`
- Double-quoted string: `"This is a string."`
- Multi-line string using triple quotes:
  ```
  '''A multi-line string
     can span several lines.'''
  ```

## String Slicing and Length

- Strings are **immutable**, meaning they cannot be changed after creation.
- You can use **slicing** to extract parts of a string.
- Example:

```python
apple = "he said, 'hi! Dhruv tum kaise ho?'"
print(apple[0:12])  # Extracts characters from index 0 to 11
print(len(apple))   # Length of the string
```

## String Methods

1. **`upper()`, `lower()`, `swapcase()`, and `capitalize()`**:
   - `upper()`: Converts the entire string to uppercase.
   - `lower()`: Converts the entire string to lowercase.
   - `swapcase()`: Swaps the case of each character (uppercase to lowercase and vice versa).
   - `capitalize()`: Capitalizes the first character of the string.

Example:
```python
nm = "he!!Man!!go!!"
print(nm.upper())  # Output: "HE!!MAN!!GO!!"
print(nm.lower())  # Output: "he!!man!!go!!"
print(nm.capitalize())  # Output: "He!!man!!go!!"
print(nm.swapcase())  # Output: "HE!!mAN!!GO!!"
```

2. **`rstrip(characters)`**:
   - Removes trailing characters (specified in the argument) from the right end of the string.

Example:
```python
print(nm.rstrip("!"))  # Output: "he!!Man!!go"
```

3. **`replace(old, new)`**:
   - Replaces occurrences of a substring with another substring.

Example:
```python
print(nm.replace("Man", "Woman"))  # Output: "he!!Woman!!go!!"
```

4. **`split(separator)`**:
   - Splits the string into a list based on the specified separator.

Example:
```python
print(nm.split("!!"))  # Output: ['he', 'Man', 'go', '']
```

5. **`count(substring)`**:
   - Returns the number of occurrences of a substring in the string.

6. **`endswith(suffix, start, end)`**:
   - Returns `True` if the string ends with the specified suffix.

7. **`startswith(prefix, start, end)`**:
   - Returns `True` if the string starts with the specified prefix.

8. **`find(substring, start, end)`**:
   - Returns the lowest index of the substring if it is found, or `-1` if not.

9. **`index(substring, start, end)`**:
   - Like `find()`, but raises a `ValueError` when the substring is not found.

Remember that the `index()` method raises an error if the substring is not found, so it's often safer to use `find()` unless you're sure the substring exists or you want to handle the exception (we'll discuss exception handling later).

Certainly! Let's explore some more string methods related to boolean checks:

## String Checks: Methods that Return Boolean Values

1. **`isalnum()`**:
   - Checks if the string is alphanumeric (contains only letters and digits).
   - Returns `True` if all characters are alphanumeric, otherwise `False`.

2. **`isalpha()`**:
   - Checks if the string contains only alphabetic characters (no spaces or digits).
   - Returns `True` if all characters are alphabetic, otherwise `False`.

3. **`islower()`** and **`isupper()`**:
   - `islower()`: Checks if all characters in the string are lowercase.
   - `isupper()`: Checks if all characters in the string are uppercase.
   - Both methods return `True` or `False`.

4. **`isprintable()`**:
   - Checks if all characters in the string are printable (i.e., visible and not control characters).
   - Returns `True` if all characters are printable, otherwise `False`.

5. **`isspace()`**:
   - Checks if the string contains only whitespace characters (spaces, tabs, newlines, etc.).
   - Returns `True` if the string is composed of whitespace, otherwise `False`.

6. **`istitle()`**:
   - Checks if the string is in title case (each word starts with an uppercase letter).
   - Returns `True` if the string is title-cased, otherwise `False`.

Example:
```python
n = "cm.;'; o3ev\n"
an = "rajurastogi123"
a = "RajuRastogi"

print(n.isalnum())  # Output: False (contains non-alphanumeric characters)
print(an.isalnum())  # Output: True (only alphanumeric characters)
print(an.isalpha())  # Output: False (contains digits)
print(a.isalpha())   # Output: True (only alphabetic characters)
print(a.islower())   # Output: False (contains uppercase letters)
print(a.isupper())   # Output: False (contains uppercase letters)
```
## String Search and Indexing

1. **`find(substring)`**:
   - The `find()` method searches for the first occurrence of a substring within a string.
   - If the substring is found, it returns the lowest index where the substring starts. If not found, it returns -1.
   - Example:
     ```python
     s = "Gantavya Bansal Is Not A Good Bboy"
     print(s.find("Bansal"))  # Output: 9 (index where "Bansal" starts)
     ```

2. **`index(substring)`**:
   - Similar to `find()`, but raises a `ValueError` if the substring is not found.
   - Example:
     ```python
     print(s.index("Is"))  # Output: 13 (index where "Is" starts)
     ```

3. **`endswith(suffix)`** and **`startswith(prefix)`**:
   - These methods check if a string ends with a specified suffix or starts with a specified prefix, respectively.
   - They return `True` or `False`.
   - Example:
     ```python
     print(s.endswith("Bboy"))    # Output: True
     print(s.startswith("Gantavya"))  # Output: True
     ```

## F-strings (Formatted String Literals)

F-strings allow you to embed expressions inside string literals. They make string formatting concise and readable.

Example:
```python
name = "Gantavya"
lname = "Bansal"
college = "GLAU"
fname = f"My name is {name} {lname} from {college}"
print(fname)  # Output: "My name is Gantavya Bansal from GLAU"
```

## Docstrings

Docstrings provide documentation for functions, classes, or modules. They are enclosed in triple quotes and appear as the first statement within a function.

Example:
```python
def square(n):
    '''Takes an integer n and returns its square.'''
    print(n**2)

square(5)  # Output: 25
print(square.__doc__)  # Output: "Takes an integer n and returns its square."
```
