
# Day 4: Decision Making 🚀

## `if-else` Statements

In Python, `if-else` statements allow you to make decisions based on conditions. Here's how they work:

1. **`if` Statement**:
   - Checks a condition. If it's true, the code block inside the `if` statement executes.
   - Example:
     ```python
     age = int(input("Enter your age: "))
     if age < 18:
         print("You are underage.")
     ```

2. **`elif` (else if) Statement**:
   - Allows you to check multiple conditions in sequence.
   - If the first condition is false, it checks the next one.
   - Example:
     ```python
     elif age == 18:
         print("Dekh kr chlaiyo beti!")
     ```

3. **`else` Statement**:
   - Executes a code block if none of the previous conditions are true.
   - Example:
     ```python
     else:
         print("Enjoy!")
     ```


## Nested `if-else` Statements

In programming, **nested `if-else` statements** refer to a structure where an `if` statement (or multiple `if` statements) is placed inside another `if` or `else` block. Essentially, it's a way to handle more complex decision-making scenarios by evaluating conditions within conditions.

Here's how it works:

1. The outer `if` statement checks a condition. If it's true, the code block inside that `if` statement executes.
2. If the outer condition is false, the program moves to the `else` block (if present) or to the next `elif` (else if) statement.
3. Within the `else` block or an `elif` statement, you can have another set of conditions (another `if` statement). This is where the nesting occurs.
4. The inner `if` statement(s) are evaluated only if the outer condition is true.

### Example:

Suppose we want to determine a student's Promotion based on their exam marks. Certainly! Nested `if-else` statements allow you to handle multiple conditions within each other. Here's an example:

```python
marks = int(input("Enter your marks: "))
if marks == 33:
    print("Just pass.")
elif marks < 33:
    if marks > 30:
        print("Can be promoted.")
    elif marks > 20:
        print("Fill compartment.")
    else:
        print("Year back.")
else:
    if marks < 60:
        print("Need to work hard.")
    elif marks < 70:
        print("Can do better.")
    elif marks < 80:
        print("Focus on studies.")
    elif marks < 90:
        print("awesome.")
    elif marks == 100:
        print("The test way easy.")
    elif marks => 90:
        print("I am impressed.")
```