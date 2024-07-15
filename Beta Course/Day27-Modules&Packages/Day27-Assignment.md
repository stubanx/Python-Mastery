---

# Python `sys` Module Assignments

## Task 1: Command Line Arguments

1. **Problem**:
   - Write a Python script that accepts a filename as a command-line argument.
   - Use the `sys.argv` list to access the provided filename.
   - Read the content of the file and display it.

2. **Real-Life Application**:
   - Imagine a text processing tool that operates on user-specified files.

## Task 2: Customizing Python Path

1. **Problem**:
   - Create a Python script that prints the current `sys.path`.
   - Modify the `sys.path` list to include a custom directory (e.g., a project folder).
   - Verify that the custom directory is now part of the path.

2. **Real-Life Application**:
   - When working on a project, ensure Python can find custom modules in a specific folder.

## Task 3: Handling Exceptions

1. **Problem**:
   - Write a Python function that performs a risky operation (e.g., dividing by zero).
   - Use `sys.exit()` to gracefully exit the program if an exception occurs.
   - Handle the exception and display an error message.

2. **Real-Life Application**:
   - In critical applications, handle unexpected errors and exit safely.

## Task 4: Byte Order Detection

1. **Problem**:
   - Create a Python script that detects the endianness (byte order) of your system.
   - Use `sys.byteorder` to determine if it's little-endian or big-endian.

2. **Real-Life Application**:
   - When working with binary data (e.g., image formats), byte order matters.

## Task 5: Auditing Hooks

1. **Problem**:
   - Explore the concept of auditing hooks using the `sys.addaudithook()` function.
   - Create a custom hook that logs information when certain events occur (e.g., function calls).

2. **Real-Life Application**:
   - In debugging or profiling tools, custom hooks can provide insights into program behavior.

---