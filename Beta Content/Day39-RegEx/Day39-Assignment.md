### **Assignment: Mastering Regular Expressions in Python through Real-Life Applications**

#### **Objective:**
This assignment aims to deepen your understanding of regular expressions (regex) by applying them to solve real-world problems. You will use Python’s `re` module to perform various text processing tasks, including validation, extraction, and manipulation.

---

### **Part 1: Basic Regex Matching**

**Task 1: Simple Email Validator**

- **Problem Statement:** Create a function `validate_email` that uses regex to check if a given string is a valid email address.
  
- **Requirements:**
  - The function should match common email formats like `username@domain.com`.
  - Use regex patterns to handle both simple and complex email formats.

- **Example Usage:**
  ```python
  def validate_email(email):
      # Your code here
      return is_valid

  print(validate_email("example@example.com"))  # Output: True
  print(validate_email("invalid-email"))  # Output: False
  ```

---

### **Part 2: Extracting Information**

**Task 2: Phone Number Extractor**

- **Problem Statement:** Write a function `extract_phone_numbers` that extracts and returns all phone numbers from a given text. Assume phone numbers are in the format `123-456-7890`.

- **Requirements:**
  - Use regex to find all phone numbers in the text.
  - Return a list of extracted phone numbers.

- **Example Usage:**
  ```python
  def extract_phone_numbers(text):
      # Your code here
      return phone_numbers

  text = "Contact me at 123-456-7890 or 987-654-3210."
  print(extract_phone_numbers(text))  # Output: ['123-456-7890', '987-654-3210']
  ```

---

### **Part 3: Data Cleaning**

**Task 3: Clean Text Data**

- **Problem Statement:** Implement a function `clean_text` that removes all special characters from a given string, keeping only alphanumeric characters and spaces.

- **Requirements:**
  - Use regex to remove any character that is not a letter, digit, or space.

- **Example Usage:**
  ```python
  def clean_text(text):
      # Your code here
      return cleaned_text

  text = "Hello, World! #Python3"
  print(clean_text(text))  # Output: "Hello World Python3"
  ```

---

### **Part 4: Advanced Regex Operations**

**Task 4: Extract Dates**

- **Problem Statement:** Write a function `extract_dates` to find all dates in the format `DD/MM/YYYY` from a given text.

- **Requirements:**
  - The function should correctly identify dates in the format `01/01/2024`, `15/08/1947`, etc.
  - Return a list of all dates found.

- **Example Usage:**
  ```python
  def extract_dates(text):
      # Your code here
      return dates

  text = "Important dates are 01/01/2024 and 15/08/1947."
  print(extract_dates(text))  # Output: ['01/01/2024', '15/08/1947']
  ```

---

### **Part 5: Parsing and Highlighting**

**Task 5: Syntax Highlighter**

- **Problem Statement:** Create a function `syntax_highlighter` that highlights Python keywords in a given code snippet. Use ANSI escape codes to highlight keywords.

- **Requirements:**
  - Define a set of Python keywords to highlight (e.g., `def`, `return`, `if`, `else`).
  - Use regex to replace keywords with highlighted versions.

- **Example Usage:**
  ```python
  def syntax_highlighter(code):
      # Your code here
      return highlighted_code

  code = """
  def greet(name):
      if name:
          return f"Hello, {name}!"
      else:
          return "Hello, World!"
  """
  print(syntax_highlighter(code))
  ```

---

### **Part 6: Real-World Contextual Problems**

**Task 6: Tokenizing Text**

- **Problem Statement:** Implement a function `tokenize_text` that tokenizes a string into words, punctuation marks, and numbers.

- **Requirements:**
  - Use regex to separate words, punctuation, and numbers into individual tokens.

- **Example Usage:**
  ```python
  def tokenize_text(text):
      # Your code here
      return tokens

  text = "Hello, World! It's 2024."
  print(tokenize_text(text))  # Output: ['Hello', ',', 'World', '!', 'It', "'", 's', '2024', '.']
  ```

---

### **Part 7: Complex Data Extraction**

**Task 7: Extract URL Links**

- **Problem Statement:** Write a function `extract_urls` that extracts all URLs from a given text. Assume URLs start with `http://` or `https://` and continue until a space or end of the line.

- **Requirements:**
  - Use regex to match URLs starting with `http://` or `https://`.

- **Example Usage:**
  ```python
  def extract_urls(text):
      # Your code here
      return urls

  text = "Visit https://example.com and http://test.org for more info."
  print(extract_urls(text))  # Output: ['https://example.com', 'http://test.org']
  ```

---