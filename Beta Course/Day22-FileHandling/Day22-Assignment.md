# File Handling Assignment

## Task 1: Reading and Displaying Content

1. Write a Python function called `read_and_display(filename)` that reads the content from a text file named `"poem.txt"` line by line and displays it on the screen.
2. Make sure to handle any file-related errors (e.g., file not found).

Example:
```python
def read_and_display(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())  # Remove extra newline characters
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")

# Test case
read_and_display("poem.txt")
```

## Task 2: Counting Non-"T" Lines

1. Create a text file named `"story.txt"` with some random lines.
2. Write a function called `count_non_t_lines(filename)` that counts the number of lines in the file that do not start with the letter "T".
3. Display the result.

Example:
```python
def count_non_t_lines(filename):
    try:
        with open(filename, "r") as file:
            non_t_lines = sum(1 for line in file if not line.startswith("T"))
            print(f"Number of non-'T' lines: {non_t_lines}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")

# Test case
count_non_t_lines("story.txt")
```

## Task 3: Word Count

1. Write a function called `word_count(filename)` that reads a text file and counts the total number of words.
2. Display the word count.

Example:
```python
def word_count(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = len(content.split())
            print(f"Total words in '{filename}': {words}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")

# Test case
word_count("article.txt")
```
