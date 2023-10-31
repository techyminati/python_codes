# Define an empty dictionary to store tasks
tasks = {}

def add_task():
    task_name = input("Enter a new task: ")
    tasks[task_name] = False  # False represents that the task is not completed

def view_tasks():
    print("\nTo-Do List:")
    for task, completed in tasks.items():
        status = "Completed" if completed else "Not Completed"
        print(f"{task} - {status}")

def mark_completed():
    task_name = input("Enter the task you want to mark as completed: ")
    if task_name in tasks:
        tasks[task_name] = True
        print(f"{task_name} marked as completed.")
    else:
        print(f"{task_name} not found in the to-do list.")

while True:
    print("\nOptions:")
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose a valid option.")
