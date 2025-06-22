todo_list = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(todo_list, start=1):
        status = "✔ Done" if task["done"] else "✘ Not Done"
        print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("Enter task: ").strip()
    if title:
        todo_list.append({"title": title, "done": False})
        print("Task added.")
    else:
        print("Task cannot be empty.")

def mark_done():
    view_tasks()
    if not todo_list:
        return
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not todo_list:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
