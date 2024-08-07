def task():
    tasks = []  # empty list 
    print("___WELCOME TO YAAD DILANE WALA APP___")

    total_task = int(input("Enter how many tasks you want to add here: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"Your today's tasks are: {tasks}")

    while True:
        operation = int(input("Choose an operation:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\n"))

        if operation == 1:
            add_task = input("Enter the task you want to add: ")
            tasks.append(add_task)
            print(f"Task '{add_task}' has been successfully added to your to-do list.")

        elif operation == 2:
            update_val = input("Enter the task you want to update: ")
            if update_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"Updated task is: '{up}'")
            else:
                print("Task not found in the list.")

        elif operation == 3:
            del_val = input("Which task do you want to delete? ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted.")
            else:
                print("Task not found in the list.")

        elif operation == 4:
            print(f"Total tasks: {tasks}")

        elif operation == 5:
            print("Exiting the task manager...")
            break

        else:
            print("Invalid input, please try again.")

task()
