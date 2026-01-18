tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit Program")

    choice = input("Enter your choice (1-4): ")

    # Add task
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully.")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    # Delete task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nCurrent Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")


            num = input("Enter task number to delete: ")

            if num.isdigit():
                num = int(num)
                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    print("\nTask deleted successfully.")
                    print("Updated task list:")

                    if len(tasks) == 0:
                        print("No tasks remaining.")
                    else:
                        for i in range(len(tasks)):
                            print(f"{i+1}. {tasks[i]}")

                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    # Exit program (with permission)
    elif choice == "4":
        confirm = input("Are you sure you want to exit? (y/n): ")
        if confirm.lower() == "y":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Exit cancelled. Returning to menu.")

    else:
        print("Invalid choice. Please try again.")

# Keeps the screen open after exit
input("\nPress Enter to close the program...")
