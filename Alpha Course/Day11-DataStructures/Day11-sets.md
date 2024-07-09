# Day 11: Sets

## Sets in Python

1. **What Is a Set?**
    - A set is an unordered collection of unique elements.
    - Key characteristics:
        - **Unordered**: The items in a set do not have a defined order.
        - **Unchangeable**: Once created, a set's items cannot be modified (but you can add or remove items).
        - **No duplicates**: Sets automatically remove duplicate values.
    - Sets are represented using curly braces `{}`.

2. **Creating a Set**:
    - You can create a set directly:
        ```python
        myset = {1, 2, 3, 4}
        ```
    - Or use the `set()` constructor:
        ```python
        myset = set([1, 2, 3, 4])
        ```

3. **Set Operations**:
    - **Union (`|`)**: Combines two sets, removing duplicates.
        ```python
        union_set = ex.union(fex)
        ```
    - **Intersection (`&`)**: Finds common elements between two sets.
        ```python
        intersection_set = ex.intersection(fex)
        ```
    - **Symmetric Difference (`^`)**: Elements present in either set but not both.
        ```python
        symmetric_diff_set = ex.symmetric_difference(fex)
        ```

4. **Set Methods**:
    - **Adding and Updating**:
        - `add(item)`: Adds an item to the set.
        - `update(iterable)`: Adds multiple items from an iterable.
    - **Removing**:
        - `remove(item)`: Removes an item (raises an error if not found).
        - `discard(item)`: Removes an item (no error if not found).
        - `pop()`: Removes and returns a random item.
    - **Set Relations**:
        - `isdisjoint(other_set)`: Checks if sets have no common elements.
        - `issuperset(other_set)`: Checks if one set contains all elements of another.
        - `issubset(other_set)`: Checks if one set is a subset of another.

5. **Frozen Sets**:
    - Immutable sets created using `frozenset()`.
    - Useful for dictionary keys or elements in other sets.
Remember, sets are powerful for handling unique data and set operations