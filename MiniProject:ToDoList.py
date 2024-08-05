# todo_list.py

def welcome_message():
    print("Welcome to the To-Do List App!")

def display_menu():
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task(tasks):
    title = input("Enter the task title: ")
    tasks.append({"title": title, "status": "Incomplete"})
    print(f"Task '{title}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task['title']} - {task['status']}")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['status'] = "Complete"
            print(f"Task {task_num} marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Task '{deleted_task['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    welcome_message()
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Quitting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
