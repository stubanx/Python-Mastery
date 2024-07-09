# Day 10: Tuples

1. **What Are Tuples?**
    - A tuple is an ordered collection of elements, similar to a list.
    - Key characteristics:
        - **Immutable**: Once created, a tuple cannot be modified (unlike lists).
        - **Ordered**: The elements in a tuple maintain their order.
        - **Allows duplicates**: You can have multiple identical elements in a tuple.
    - Tuples are written using parentheses `( )`.

2. **Creating a Tuple**:
    - To create a tuple, enclose comma-separated values within parentheses:
        ```python
        mytuple = (1, 2, 34, 36, 690, 7)
        print(type(mytuple), mytuple)
        ```
    - Output: `<class 'tuple'> (1, 2, 34, 36, 690, 7)`

3. **Tuple Operations**:
    - **Slicing**: Extracting parts of a tuple:
        ```python
        tup2 = mytuple[1:5]  # Slice from index 1 to 4
        ```
    - **Concatenation**: Combining two tuples:
        ```python
        combined_tuple = mytuple + (10, 20)
        ```
    - **Finding Index**:
        ```python
        index_of_34 = mytuple.index(34)  # Returns the index of 34
        ```

4. **Tuple Length**:
    - To find the number of items in a tuple, use the `len()` function:
        ```python
        length = len(mytuple)
        ```

5. **Tuple with One Item**:
    - To create a tuple with only one item, add a comma after the item:
        ```python
        single_item_tuple = ("apple",)
        ```

6. **Tuple Items and Data Types**:
    - Tuple items can be of any data type (strings, integers, booleans, etc.):
        ```python
        mixed_tuple = ("abc", 34, True, 40, "male")
        ```

7. **Type of a Tuple**:
    - From Python's perspective, tuples are objects with the data type 'tuple':
        ```python
        print(type(mytuple))  # Output: <class 'tuple'>
        ```

8. **Using the `tuple()` Constructor**:
    - You can also create a tuple using the `tuple()` constructor:
        ```python
        thistuple = tuple(("apple", "banana", "cherry"))
        ```

Tuples are handy when you need to store data that shouldn't change. 