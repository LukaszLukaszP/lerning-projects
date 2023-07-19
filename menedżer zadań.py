def new_task():
    try:
        with open("tasks.txt", 'a') as file:
            task = input("enter a new task: ")
            file.write(task + '\n')
    except FileExistsError:
        return print("file not found")


def read_tasks():
    try:
        with open("tasks.txt", "r") as file:
            print(file.readlines())
    except FileExistsError:
        return print("file not found")


def remove_task():
    task_to_remove = input("enter a task to remove")
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()

        with open("tasks.txt", "w") as file:
            for line in lines:
                if line.strip() not in task_to_remove:
                    file.write(line)
    except FileExistsError:
        return print("file not found")


def check_action(action):
    actions = ['1', '2', '3', '4']
    while action not in actions:
        return True
    return False


def end_program():
    action = choose_action()
    if action == "4":
        return False
    else:
        return True


def choose_action():
    action = input("""what you want to do?
    1 - create new task
    2 - read tasks
    3 - remove task
    4 - end program
    : """)
    while check_action(action):
        action = input("""what you want to do?
        1 - create new task
        2 - read tasks
        3 - remove task
        4 - end program
        : """)
    return action


while True:
    action = choose_action()
    if action == '1':
        new_task()
    elif action == '2':
        read_tasks()
    elif action == '3':
        remove_task()
    elif action == '4':
        end_program()
