tasks = [] 

while True:
    print("\n--- TO DO LIST ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Edit task")
    print("4. Remove task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print("Task added.")

    elif choice == "3":
        if not tasks:
            print("No tasks to edit.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                num = int(input("Enter task number to edit: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1] = input("Enter new task: ")
                    print("Task updated.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    print("Task removed.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Wrong choice. Try again.")