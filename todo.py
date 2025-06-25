# todo.py

FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print(" Task added: {task}")

def view_tasks(tasks):
    if not tasks:
        print(" No tasks found.")
    else:
        print(" Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑️ Task removed: {removed}")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print(" Exiting... Your tasks are saved.")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
