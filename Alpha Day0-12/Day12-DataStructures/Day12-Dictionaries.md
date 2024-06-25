# Day 12: Dictionaries

1. **What Is a Dictionary?**
    - A dictionary is a built-in data structure in Python that stores data in key-value pairs.
    - Key characteristics:
        - **Ordered (from Python 3.7+)**: Dictionaries maintain the order of insertion.
        - **Changeable**: You can modify, add, or remove items after creating a dictionary.
        - **No duplicates**: Each key is unique, and duplicate keys are not allowed.
    - Dictionaries are useful for mapping one value (the key) to another (the value).

2. **Creating a Dictionary**:
    - You can define a dictionary using curly braces `{}`:
        ```python
        my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
        ```
    - Or use the `dict()` constructor:
        ```python
        my_dict = dict(brand="Ford", model="Mustang", year=1964)
        ```

3. **Accessing Dictionary Items**:
    - Retrieve values using their keys:
        ```python
        print(my_dict["brand"])  # Output: "Ford"
        ```

4. **Dictionary Methods**:
    - `get(key)`: Safely retrieves the value for a given key (returns `None` if key not found).
    - `keys()`: Returns a view of all keys.
    - `items()`: Returns a view of key-value pairs.
    - `update(other_dict)`: Merges another dictionary into the current one.
    - `popitem()`: Removes and returns the last key-value pair.
    - `clear()`: Removes all items from the dictionary.

5. **Dictionary Length**:
    - Use `len(my_dict)` to get the number of key-value pairs.

6. **Data Types in Dictionary Items**:
    - Dictionary values can be of any data type (strings, integers, booleans, lists, etc.).

7. **Type of a Dictionary**:
    - From Python's perspective, dictionaries are objects with the data type 'dict':
        ```python
        print(type(my_dict))  # Output: <class 'dict'>
        ```

8. **Real-Life Analogy**:
    - Think of a dictionary like a real-world dictionary where words (keys) are associated with their meanings (values).

Remember, dictionaries are preffered for organizing and retrieving data based on keys.