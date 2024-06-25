# Day 9: Lists

 **Lists**:
    - A list is a versatile data structure in Python that allows you to store multiple items (elements) in a single variable.
    - Key characteristics:
        - **Ordered**: The elements in a list maintain their order of insertion.
        - **Changeable**: You can modify the contents of a list after it's created.
        - **Allows duplicates**: You can have multiple identical elements in a list.
    - Creating a list:
        ```python
        mylist = ["apple", "banana", "cherry"]
        print(mylist)  # Output: ['apple', 'banana', 'cherry']
        ```
    - Common list methods:
        - `append(item)`: Adds an item to the end of the list.
        - `sort()`: Sorts the list in ascending order (modifies the original list).
        - `reverse()`: Reverses the order of the list (modifies the original list).
        - `count(item)`: Returns the number of occurrences of an item.
        - `index(item)`: Returns the index of the first occurrence of an item.
        - `insert(index, item)`: Inserts an item at a specific position.
        - `extend(iterable)`: Merges two lists by adding elements from the iterable.
    - Example:
        ```python
        mylist.append(34)  # Adds 34 to the end
        mylist.sort()      # Sorts the list
        mylist.reverse()   # Reverses the order
        print(mylist.count(34))  # Prints the count of occurrences of 34
        ```

1. **List Indexing and Slicing**:
    - You can access individual elements in a list using their index. The index starts from 0 for the first element.
    - Example:
        ```python
        mylist = ["apple", "banana", "cherry"]
        print(mylist[0])  # Output: "apple"
        ```
    - You can also slice a list to get a portion of it:
        ```python
        print(mylist[1:3])  # Output: ["banana", "cherry"]
        ```

2. **List Comprehensions**:
    - List comprehensions provide a concise way to create lists based on existing lists.
    - Example (squares of numbers from 0 to 9):
        ```python
        squares = [x**2 for x in range(10)]
        print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        ```

3. **Nested Lists (List of Lists)**:
    - You can have lists within lists (nested lists).
    - Example:
        ```python
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print(matrix[1][2])  # Output: 6
        ```

4. **List Membership and Length**:
    - To check if an item exists in a list:
        ```python
        if "banana" in mylist:
            print("Found banana!")
        ```
    - To get the length of a list:
        ```python
        print(len(mylist))  # Output: 3
        ```

Remember, Python lists are incredibly versatile, and there's always more to explore! 😊