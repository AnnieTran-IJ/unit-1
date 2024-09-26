
#color indication:
end_code = "\033[00m"
green = "\33[0;32m"
red = "\33[0;31m"
underline_start = "\033[4m"
underline_end = "\033[0m"
bold_purple = "\33[1;35m"
bold_white = "\33[1;37m"
bold_blue = "\33[1;34m"
#to-do list
tasks = []

def add_task():
    task = input("What is your new task? ")
    tasks.append((task,"[ ]"))
    print(f"{green}Task `{task}` added successfully.{end_code}\n")

def mark_as_done():
    view_task()
    if not tasks:
        return

    try:
        task_to_mark = int(input("Please enter the number of which task you want to mark as done: ")) - 1
        if task_to_mark >= 0 and task_to_mark < len(tasks):
            task_name, _ = tasks[task_to_mark]
            # Change status to done `[✓]`
            tasks[task_to_mark] = (task_name, "[✓]")
            print(f"{green}Task `{task_name}` has been marked as done.{end_code}\n")
        else:
            print(f"{red}Task number {task_to_mark + 1} was not found.{end_code}")
    except ValueError:
        print(f"{red}Invalid input. Please try again.{end_code}")

def view_task():
    if not tasks:
        print("There are no tasks currently.\n")
        return
    else:
        incomplete_tasks = []
        for i, (task, status) in enumerate(tasks):
            if status == "[ ]":
                incomplete_tasks.append((i, task, status))

        completed_tasks = []
        for i, (task, status) in enumerate(tasks):
            if status == "[✓]":
                completed_tasks.append((i, task, status))

        print(f"{bold_purple}Incomplete Tasks:\n{end_code}")
        if incomplete_tasks:
            for index, (i, task, status) in enumerate(incomplete_tasks, 1):
                print(f"Task {status} #{i+1}. {task}")
            else:
                print("No completed tasks.\n")

        print(f"{bold_blue}\nCompleted Tasks:{end_code}")
        if completed_tasks:
            for index, (i, task, status) in enumerate(completed_tasks, 1):
                print(f"Task {status} #{i+1}. {task}")
        else:
            print("No completed tasks.\n")