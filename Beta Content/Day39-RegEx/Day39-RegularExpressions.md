# Day 39
### **Understanding Regular Expressions (Regex) in Python: A Comprehensive Guide**

Regular expressions (often abbreviated as **regex** or **regexp**) are sequences of characters that form a search pattern. They are used for string matching and manipulation. Python's `re` module provides support for regular expressions, allowing you to perform complex string operations efficiently.

---

### **1. What Are Regular Expressions?**

**Regular expressions** are like special codes that describe search patterns in text. Imagine you have a text document and you want to find every occurrence of a specific pattern, like a word, a number, or even a complex combination of characters. Regular expressions allow you to define this pattern and find all matches in the text.

**Example:** If you want to find all instances of the word "cat" in a document, a simple regular expression could be `"cat"`.

---

### **2. Basic Concepts of Regular Expressions**

#### **2.1. Matching Literal Characters**

- **`"cat"`** matches exactly the string "cat".
- **Case-Sensitivity:** Regex is case-sensitive by default. `"Cat"` will not match `"cat"`.

#### **2.2. Special Characters in Regex**

Special characters have unique meanings in regex. Some commonly used ones include:

- **`.` (dot):** Matches any single character except a newline.
  - Example: **`"c.t"`** matches `"cat"`, `"cot"`, `"cut"`, etc.
- **`^`:** Matches the start of a string.
  - Example: **`"^cat"`** matches `"cat"` only if it appears at the beginning of a string.
- **`$`:** Matches the end of a string.
  - Example: **`"cat$"`** matches `"cat"` only if it appears at the end of a string.
- **`*`:** Matches zero or more occurrences of the preceding element.
  - Example: **`"ca*t"`** matches `"ct"`, `"cat"`, `"caat"`, etc.
- **`+`:** Matches one or more occurrences of the preceding element.
  - Example: **`"ca+t"`** matches `"cat"`, `"caat"`, but not `"ct"`.
- **`?`:** Matches zero or one occurrence of the preceding element.
  - Example: **`"ca?t"`** matches `"ct"` and `"cat"`.

#### **2.3. Character Classes**

Character classes let you define a set of characters to match.

- **`[abc]`:** Matches any one of the characters `a`, `b`, or `c`.
  - Example: **`"[cb]at"`** matches `"cat"` and `"bat"`, but not `"dat"`.
- **`[a-z]`:** Matches any lowercase letter.
  - Example: **`"[a-z]"`** matches any lowercase letter from `a` to `z`.
- **`[0-9]`:** Matches any digit.
  - Example: **`"[0-9]"`** matches any digit from `0` to `9`.
- **`[^abc]`:** Matches any character except `a`, `b`, or `c`.
  - Example: **`"[^ab]at"`** matches `"cat"` but not `"aat"` or `"bat"`.

---

### **3. Working with Regular Expressions in Python**

To use regular expressions in Python, you need to import the `re` module.

#### **3.1. Basic String Matching**

**Example:**

```python
import re

# Search for the word 'cat'
text = "The cat sat on the mat."
match = re.search(r"cat", text)
if match:
    print("Found:", match.group())  # Output: Found: cat
```

- **`re.search(pattern, string)`:** Searches for the first occurrence of the pattern in the string.
- **`match.group()`**: Returns the matched string.

#### **3.2. Finding All Matches**

**Example:**

```python
import re

# Find all occurrences of the word 'cat'
text = "The cat sat on the mat. Another cat was there too."
matches = re.findall(r"cat", text)
print("Found:", matches)  # Output: Found: ['cat', 'cat']
```

- **`re.findall(pattern, string)`:** Returns a list of all matches of the pattern in the string.

#### **3.3. Replacing Matches**

**Example:**

```python
import re

# Replace 'cat' with 'dog'
text = "The cat sat on the mat."
new_text = re.sub(r"cat", "dog", text)
print("Replaced:", new_text)  # Output: Replaced: The dog sat on the mat.
```

- **`re.sub(pattern, replacement, string)`:** Replaces all occurrences of the pattern with the replacement in the string.

---

### **4. Advanced Regular Expressions**

#### **4.1. Grouping and Capturing**

Parentheses `()` allow you to group parts of a regex and capture the matched text.

**Example:**

```python
import re

# Grouping example
text = "My phone number is 123-456-7890."
match = re.search(r"(\d{3})-(\d{3})-(\d{4})", text)
if match:
    print("Area code:", match.group(1))  # Output: Area code: 123
    print("Main number:", match.group(2))  # Output: Main number: 456
    print("Line number:", match.group(3))  # Output: Line number: 7890
```

- **`(\d{3})`**: Captures a group of three digits.
- **`match.group(n)`**: Returns the nth captured group.

#### **4.2. Using `|` for Alternation**

The `|` operator allows you to match one pattern or another.

**Example:**

```python
import re

# Match 'cat' or 'dog'
text = "I have a cat and a dog."
matches = re.findall(r"cat|dog", text)
print("Found:", matches)  # Output: Found: ['cat', 'dog']
```

#### **4.3. Lookahead and Lookbehind Assertions**

Lookahead and lookbehind assertions allow you to match a pattern only if it's followed or preceded by another pattern, without including that pattern in the match.

- **Lookahead (`?=`):** Ensures a pattern is followed by another pattern.

  **Example:**

  ```python
  import re

  # Match 'cat' only if followed by 's'
  text = "cats are great, but so are dogs."
  match = re.search(r"cat(?=s)", text)
  if match:
      print("Found:", match.group())  # Output: Found: cat
  ```

- **Lookbehind (`?<=`):** Ensures a pattern is preceded by another pattern.

  **Example:**

  ```python
  import re

  # Match 's' only if preceded by 'cat'
  text = "cats are great."
  match = re.search(r"(?<=cat)s", text)
  if match:
      print("Found:", match.group())  # Output: Found: s
  ```

---

### **5. Real-Life Applications of Regular Expressions**

#### **5.1. Validating Email Addresses**

**Problem:** Validate if a string is a correctly formatted email address.

**Example:**

```python
import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

print(is_valid_email("test@example.com"))  # Output: True
print(is_valid_email("invalid-email"))  # Output: False
```

- **Explanation:** The pattern ensures the email contains characters, an "@" symbol, a domain name, and a valid top-level domain.

#### **5.2. Extracting Data from Text**

**Problem:** Extract phone numbers from a text document.

**Example:**

```python
import re

text = """
John's number is 123-456-7890.
Jane's number is 987-654-3210.
"""

# Pattern to match phone numbers
pattern = r"(\d{3})-(\d{3})-(\d{4})"
matches = re.findall(pattern, text)

for match in matches:
    print("Phone Number:", "-".join(match))
```

- **Explanation:** The regex captures and extracts phone numbers in the `123-456-7890` format.

#### **5.3. Parsing and Cleaning Data**

**Problem:** Remove all special characters from a string, keeping only alphanumeric characters and spaces.

**Example:**

```python
import re

def clean_text(text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text)

text = "Hello, World! This is a test... #cleaning@text"
cleaned_text = clean_text(text)
print("Cleaned:", cleaned_text)  # Output: "Hello World This is a test cleaningtext"
```

- **Explanation:** The pattern `[^a-zA-Z0-9\s]` matches any character that is not a letter, digit, or space, and replaces it with an empty string.

---

### **6. Extreme Use Cases of Regular Expressions**

#### **6.1. Tokenizing Text**

**Problem:** Tokenize a string into words, punctuation marks, and numbers.

**Example:**

```python


import re

def tokenize(text):
    pattern = r"\w+|[^\w\s]"
    return re.findall(pattern, text)

text = "Hello, World! It's 2024."
tokens = tokenize(text)
print("Tokens:", tokens)
# Output: ['Hello', ',', 'World', '!', 'It', "'", 's', '2024', '.']
```

- **Explanation:** The pattern `\w+|[^\w\s]` matches words, punctuation marks, and numbers separately, effectively tokenizing the text.

#### **6.2. Building a Simple Syntax Highlighter**

**Problem:** Highlight Python keywords in a code snippet.

**Example:**

```python
import re

def highlight_keywords(code):
    keywords = r"\b(def|return|if|else|for|while|import|as|from)\b"
    return re.sub(keywords, r"\033[1;31m\1\033[0m", code)

code = """
def greet(name):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, World!"
"""

highlighted_code = highlight_keywords(code)
print(highlighted_code)
```

- **Explanation:** The pattern matches Python keywords, and `re.sub` replaces them with the highlighted version using ANSI escape codes.

---

### **7. Summary**

Regular expressions are powerful tools for text processing in Python. Whether you're validating input, extracting data, or manipulating strings, regex can help you perform complex tasks efficiently. From basic patterns to advanced assertions, regex opens up a world of possibilities for working with text.

- **Practice:** The key to mastering regular expressions is practice. Try writing regex patterns for different problems to reinforce your understanding.
- **Tools:** Tools like [regex101.com](https://regex101.com/) can help you test and debug regular expressions interactively.

---

With this guide, you should be well-equipped to tackle regular expressions from basic to advanced levels, and use them effectively in real-life applications.