# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added: ", task)

# Function to view all tasks in the list
def view_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks to display.")

# Function to delete a task from the list
def delete_task(task_number):
    if task_number > 0 and task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print("Deleted task:", deleted_task)
    else:
        print("Invalid task number.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_number = int(input("Enter the task number to delete: "))
        delete_task(task_number)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
