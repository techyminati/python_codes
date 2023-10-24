# Initialize an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to view the to-do list
def view_tasks():
    if todo_list:
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    else:
        print("To-Do List is empty.")

# Function to remove a task from the to-do list
def remove_task(task_index):
    if task_index >= 1 and task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task index to remove: "))
        remove_task(task_index)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select a valid option.")
