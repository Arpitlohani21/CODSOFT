# To-Do List Application (Task 1)
# Author: [Your Name]
# Internship: CODSOFT

todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter new task: ")
    todo_list.append(task)
    print("Task added successfully.")

def update_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_num < len(todo_list):
            new_task = input("Enter updated task: ")
            todo_list[task_num] = new_task
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(todo_list):
            deleted = todo_list.pop(task_num)
            print(f"Task '{deleted}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
