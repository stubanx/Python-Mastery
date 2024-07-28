# Day 6: For Loop

In Python, a **for loop** is used to iterate over a sequence of values. Let's break down the key points:

1. **Syntax**:
    - The basic syntax of a `for` loop is as follows:
      ```python
      for item in sequence:
          # Code block to execute for each item
          # ...
      ```
    - Here's what each part means:
        - `item`: An iterator variable that takes on each value from the `sequence`.
        - `sequence`: An iterable object (e.g., list, string, tuple, range) over which the loop iterates.

2. **Example with a List**:
    - Suppose we have a list of fruits:
      ```python
      fruits = ["apple", "banana", "cherry"]
      ```
    - We can use a `for` loop to print each fruit:
      ```python
      for fruit in fruits:
          print(fruit)
      ```
    - Output:
      ```
      apple
      banana
      cherry
      ```

3. **Looping Through a String**:
    - Even strings are iterable objects. For example:
      ```python
      word = "banana"
      for letter in word:
          print(letter)
      ```
    - Output:
      ```
      b
      a
      n
      a
      n
      a
      ```

4. **The `range()` Function**:
    - To loop a specific number of times, use the `range()` function:
      ```python
      for num in range(5):  # Loops from 0 to 4
          print(num)
      ```
    - Output:
      ```
      0
      1
      2
      3
      4
      ```

5. **`break` and `continue` Statements**:
    - `break`: Stops the loop prematurely.
    - `continue`: Skips the current iteration and moves to the next.
    - Example using `break`:
      ```python
      for fruit in fruits:
          if fruit == "banana":
              break
          print(fruit)
      ```
    - Output (stops when it encounters "banana"):
      ```
      apple
      ```
    - Example using `continue`:
      ```python
      for fruit in fruits:
          if fruit == "banana":
              continue
          print(fruit)
      ```
    - Output (skips "banana"):
      ```
      apple
      cherry
      ```

6. **`else` in a `for` Loop**:
    - The `else` block executes when the loop completes normally (without a `break`):
      ```python
      for num in range(6):
          print(num)
      else:
          print("Finally finished!")
      ```
    - Output:
      ```
      0
      1
      2
      3
      4
      5
      Finally finished!
      ```

Remember, `for` loops are versatile and allow you to automate repetitive tasks efficiently. Feel free to explore more complex scenarios! 😊🚀


7. **`pass` Statement**:
    - The `pass` statement is a **no-op** (no operation) placeholder in Python.
    - It does nothing when executed and serves as a syntactical requirement in certain situations.
    - Common use cases for `pass` include:
        - Placeholder for future code (when you're writing a function or class but haven't implemented its logic yet).
        - Ensuring that a block of code remains syntactically valid (e.g., in an empty `if` or `while` block).
        ```python
        var = 10
        while var > 0:
            if var == 5:
                break
            print(var)
            var -= 1

        while var > 0:
            if var == 5:
                continue
            var -= 1
            print(var)
        ```