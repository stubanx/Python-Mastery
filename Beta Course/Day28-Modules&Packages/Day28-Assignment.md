

---

# Python `os` Module Assignments

## Task 1: Working with Directories

1. **Problem**:
   - Write a Python script that lists all files in the current working directory.
   - Use `os.getcwd()` and `os.listdir()` to achieve this.
   - Display the filenames.

2. **Real-Life Application**:
   - Imagine building a file organizer tool that categorizes files based on their extensions.

## Task 2: Creating a New Directory

1. **Problem**:
   - Create a Python function that takes a directory name as input.
   - Use `os.mkdir(directory_name)` to create a new directory.
   - Verify that the directory is created.

2. **Real-Life Application**:
   - When setting up a new project, create a dedicated folder to organize related files.

## Task 3: Checking File Existence

1. **Problem**:
   - Write a Python function that checks if a given file exists.
   - Use `os.path.exists(path)` to verify file existence.
   - Return a boolean value.

2. **Real-Life Application**:
   - Before downloading a file from the internet, check if it already exists locally.

## Task 4: Environment Variables

1. **Problem**:
   - Create a Python script that prints all environment variables.
   - Access `os.environ` to retrieve the environment variables.
   - Display the variable names and their values.

2. **Real-Life Application**:
   - Environment variables store system-wide settings, such as paths and configuration options.

## Task 5: Running System Commands

1. **Problem**:
   - Write a Python function that runs an external system command.
   - Use `os.system(command)` to execute a shell command.
   - Example: Run `ls` (list files) or `mkdir` (create a directory).

2. **Real-Life Application**:
   - Automate repetitive tasks by invoking system commands from Python.

---