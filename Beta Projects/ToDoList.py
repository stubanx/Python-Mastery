# Code Overview:

# File Handling Initialization:
# The code begins by initializing an empty list listdo and a variable a set to None.
# It then enters a loop where the user is prompted to either open an existing file or create a new one.
# File Opening or Creation:

# Open Existing File:
# If the user chooses to open an existing file (by inputting 'o'), they are prompted to enter the filename.
# The code attempts to open and read the file, storing each line as an item in the listdo list.
# If the file is not found, an error message is displayed.
# Create New File:
# If the user chooses to create a new file (by inputting 'n'), the filename is noted, and a success message is displayed.
# If an invalid choice is made, the user is prompted again.

# Command Instructions:
# After successfully opening or creating a file, the user is greeted with a welcome message and a list of available commands:
# add- <task>: Add a task to the list.
# remove- <task>: Remove a task from the list.
# show- list: Display all tasks in the list.
# save- list: Save the list to the file.
# exit- list: Exit the program (with a reminder to save changes).

# Task Management Loop:
# The code then enters a loop where it continuously prompts the user to enter an operation until they choose to exit.
# Add Task:
# The add command adds a specified task to the listdo list and confirms the addition.
# Remove Task:
# The remove command removes a specified task from the listdo list and confirms the removal.
# Show List:
# The show command displays all tasks in the listdo list, numbered sequentially.
# Exit Program:
# The exit command prompts for confirmation before breaking the loop and ending the program.
# Save List:
# The save command writes the current list of tasks to the specified file and confirms the save.
# If an invalid command is entered, an error message is displayed.

a=None
listdo=[]
print("TODOLIST @CODESOFT cc%GANTAVYA BANSAL")
while(a!=1):
    file=input("Open existing(o)/create new(n):")
    filename=input("Enter the file name:")+'.txt'
    
    if file.lower()=='o':
        try:
            with open(filename,'r') as f:
                listdo=f.read().splitlines()
                a=1
                print(f"{filename} found")

        except FileNotFoundError:
            print("Error! File not found")

    elif file.lower()=='n':
        # filename=input("Enter thr file name to be created:")
        print(f"{filename} created sucessfully")
        a=1
    
    else:
        print("Invalid choice")


print('''Hey! Welcome to our todolist powered by CODESOFT
      Here are the commands you can use:
      'add- <task>' to add a task
      'remove- <task>' to remove a task
      'show- list' to view your list
      'save- list' to save your list
      'exit- list' to exit(Make sure to save changes before exiting!)''')

operation=None
while(operation!='exit'):
    operation,task=map(str,input(f"Enter your operation or do 'save- {filename}' and 'exit- {filename}' to quit: ").split('-'))
    
    if operation.lower()=='add':
        listdo.append(task)
        print(f"Task '{task}' added successfully")
    
    elif operation.lower()=='remove':
        listdo.remove(task)
        print(f"Task '{task}' removed successfully")
    
    elif operation.lower()=='show':
        for i in range(0,len(listdo)):
            print(i+1,listdo[i])
   
    elif operation.lower()=='exit':
        if(input("confirm exit?? enter 'yes' else 'no': ")=='y'):
            print(f"Succoess! {filename} closed")
            break

        else:
            continue
    
    elif operation.lower()=='save':
        with open(filename, 'w') as f:
            for item in listdo:
                f.write("%s\n" %item)
        print(f"{filename} saved")

    else:
        print("Invalid input")


