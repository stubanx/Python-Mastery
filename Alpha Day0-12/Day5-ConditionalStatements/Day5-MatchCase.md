# Day 5: Decision Making 🚀

The `match` case statements in Python 3.10+ provide a more concise way to handle multiple conditions. Let's break down the example provided:

    ```python
    x = int(input("Enter the value of 'x': "))
    match x:
        case 0:
            print("x is 0")
        case 1:
            print("x is 1")
        case _ if x != 80:
            print("Not 80")
        case _:
            print("Other value")
    ```

1. First, the user inputs a value for `x`.
2. The `match` statement evaluates the value of `x` against several cases.
3. If `x` is equal to 0, it prints "x is 0."
4. If `x` is equal to 1, it prints "x is 1."
5. If `x` is not equal to 80 (indicated by `_ if x != 80:`), it prints "Not 80."
6. If none of the above conditions match (indicated by `_:`), it prints "Other value."

This construct is particularly useful when you have multiple conditions to check against a single value. It's more concise than using a series of `if` and `elif` statements.

Remember that the `match` statement is available in Python 3.10 and later versions. If you're using an older version of Python, you'll need to use traditional `if` and `elif` statements instead.
