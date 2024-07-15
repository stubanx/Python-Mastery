# Day-22
1. **What Is File Handling?**
   - **Definition**: File handling refers to reading from and writing to files on your computer.
   - **Purpose**: It allows you to store and retrieve data persistently, even after your program exits.

2. **Basic File Operations**:
   - **Opening a File**: Use the `open()` function to open a file. Specify the filename and the mode (e.g., read, write, append).
   - **Reading from a File**: Use `file.read()` to read the entire file or `file.readline()` to read one line at a time.
   - **Writing to a File**: Use `file.write("content")` to add content to a file.
   - **Closing a File**: Always close the file using `file.close()` when you're done.

3. **Example: Reading from a File**
   ```python
   # Open the file in read mode
   with open("my_file.txt", "r") as file:
       content = file.read()
       print(content)
   ```

4. **Advanced Concepts**:
   - **Context Managers**: Use `with open(...) as file:` to automatically close the file when you're done.
   - **Modes**: Modes include `"r"` (read), `"w"` (write), `"a"` (append), and more.
   - **Binary Files**: You can read/write binary files (e.g., images) using `"rb"` and `"wb"` modes.
   - **Exception Handling**: Handle file-related errors using `try` and `except`.

5. **Real-Life Applications**:
   - **Log Files**: Store application logs for debugging.
   - **Data Persistence**: Save user preferences, game progress, or settings.
   - **CSV Files**: Read/write data in tabular format.
   - **Configuration Files**: Store program settings.

Remember, file handling is versatile, but be cautious about security and error handling. Happy coding! 🚀
