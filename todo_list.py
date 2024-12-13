'''
Build a simple command-line to-do list manager. The user can add tasks, remove tasks, and view all tasks. Tasks can be saved to a text file.
'''
# Main function to manage the To-Do List.
def todo_list():
    tasks = load_tasks() # Load the existing tasks from the text file
    while True:
        # Display the menu with options for the user
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        # Prompt user for their choice
        choice = input("Enter choice what you want to do: ")
        
        if choice == '1':
            show_tasks(tasks)
        if choice == '2':
            task = input("Enter task: ")
            add_task(tasks, task)
        if choice == '3':
            show_tasks(tasks)
            task_num = int(input("Enter task number to remove: "))
            remove_task(tasks, task_num)
        if choice == '4':
            print("Exiting...")
            break

# Function to take data from the txt file
def load_tasks():
    try:
        # Try to open the tasks.txt file and read its contents
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            # Strip newline characters from each task and return a list
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return[]

# Function to display all tasks
def show_tasks(tasks):
    if tasks:
        # If there are tasks, display them
        print("\nYour To-do List: ")
        # Enumerate tasks and print each one with its number
        for index, task in enumerate(tasks,1):
            print(f"{index}.{task}")
    else:
        # If there are no tasks, inform the user
        print("No tasks available.")

# Function to add a new task to the list
def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)

# Function to remove a task from the list by its number
def remove_task(tasks, task_num):
    # Check if the task number is valid (within range)
    if 0<task_num <= len(tasks):
        tasks.pop(task_num - 1)
        save_tasks(tasks)
    else:
        print("Invalid task number")

# Function to save tasks to the text file
def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(f"{task}\n")
    
todo_list()