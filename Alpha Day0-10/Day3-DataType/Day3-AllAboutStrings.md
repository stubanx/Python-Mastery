# Day 2: All About Srings:
## String Basics:
- Strings can be enclosed in single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`).
- Example: 
'Hello, Python!',
"This is a string.",
'''A multi-line string
    can span several lines.'''
    
## String Slicing and Length:
- Strings are immutable (cannot be changed after creation).
- Use slicing to extract parts of a string.
- Example:

apple = "he said, ' hi! Dhruv tum kaise ho?'"
print(apple[0:12])  # Extracts characters from index 0 to 11
print(len(apple))   # Length of the string
        

## String Methods:
- `upper()`, `lower()`, `swapcase()` and `capitalize()`: Modify case.
- `rstrip(characters)`: Remove trailing characters.
- `replace(old, new)`: Replace occurrences of a substring.
- `split(separator)`: Split the string into a list based on the separator.

nm = "he!!Man!!go!!"
print(nm.upper(), nm.lower(), nm.capitalize(), nm.swapcase())
print(nm.rstrip("!"))
print(nm.replace("Man", "Woman"))
print(nm.split("!!"))
- *NOTE-* `start, end` gives the range of string in which the operation is to be performed in form of index values.
- `count(substring)`: Returns the number of occurrences of a substring.
- `endswith(suffix, start, end)`: Returns True if the string ends with the specified suffix.
- `startswith(prefix, start, end)`: Returns True if the string starts with the specified prefix.
- `find(substring, start, end)`: Returns the lowest index of the substring if it is found.
- `index(substring, start, end)`: Like find(), but raises ValueError when the substring is not found.

nm = "he!!Man!!go!!"
print(nm.count("!"))  # Output: 6
print(nm.endswith("!!"))  # Output: True
print(nm.endswith("go", 4, 11))  # Output: False
print(nm.startswith("!!"))  # Output: False
print(nm.startswith("go", 4, 11))  # Output: True
print(nm.find("go"))  # Output: 8
print(nm.find("ish"))  # Output: Negative
print(nm.index("go"))  # Output: 8
try:
    print(nm.index("ish"))  # This will raise a ValueError as "ish" is not in the string.
except ValueError as e:
    print(e)  # Output: substring not found
Remember, the `index()` method will raise an error if the substring is not found, so it's often safer to use `find()` unless you're sure the substring exists or you want to handle the exception(We will discuss exception handling later).

## String Checks:
### Methods that return boolean values:
- `isalnum()`: Checks if the string is alphanumeric (contains only letters and digits).
- `isalpha()`: Checks if the string contains only alphabetic characters.
- `islower()`, `isupper()`: Check letter case.
- `isprintable()`: Checks if all characters are printable.
- `isspace()`: Checks if the string contains only whitespace.
- `istitle()`: Checks if the string is in title case.
- Example:

n = "cm.;'; o3ev\n"
an = "rajurastogi123"
a = "RajuRastogi"
print(n.isalnum(), an.isalnum())
print(an.isalpha(), a.isalpha())
print(a.islower(), a.isupper())

5. **String Search and Indexing**:
    - `find(substring)`: Finds the first occurrence of a substring (returns -1 if not found).
    - `index(substring)`: Finds the index of a substring (raises an error if not found).
    - `endswith(suffix)`, `startswith(prefix)`: Check if the string ends or starts with a given substring.
    - Example:
        ```python
        s = "Gantavya Bansal Is Not A Good Bboy"
        print(s.find("Bansal"))
        print(s.index("Is"))
        print(s.endswith("Bboy"))
        print(s.startswith("Gantavya"))
        ```

1. **f-strings**:
   - You've used an f-string to create a formatted string. F-strings (formatted string literals) allow you to embed expressions inside string literals, using curly braces `{}`.
   - In your example:
     ```python
     name = "Gantavya"
     lname = "Bansal"
     college = "GLAU"
     fname = f"My name is {name} {lname} from {college}"
     print(fname)
     ```
     The output will be: `My name is Gantavya Bansal from GLAU`.

2. **Docstrings**:
   - Docstrings are used to provide documentation for functions, classes, or modules.
   - They are enclosed in triple quotes (`'''` or `"""`) and appear as the first statement within a function.
   - Example:
     ```python
     def square(n):
         '''Takes an integer n and returns its square.'''
         print(n**2)
     square(5)
     print(square.__doc__)
     ```
     The docstring explains what the `square` function does.