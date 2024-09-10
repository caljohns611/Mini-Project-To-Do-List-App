def menu():
    print("""
Welcome to the To-Do App
    
Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit        
""")
    
def add_task(task_list):
    title = input("Enter a task (default is 'Incomplete'): ")
    if not title.strip():
        title = "Incomplete"
    task_list.append({"title": title, "status": "Incomplete"})
    print(f"Added task: {title}")

def view_tasks(task_list):
    if not task_list:
        print("There are no tasks at the moment.")
    else:
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task['title']} - {task['status']}")

def complete_task(task_list):
    view_tasks(task_list)
    try:
        task_number = int(input("Please enter a task number you want to complete: "))
        if 0 <= task_number < len(task_list):
            if task_list[task_number]['status'] == "Complete":
                print("This task is already complete.")
            else:
                task_list[task_number]['status'] = "Complete"
                print(f"Mark task as complete: {task_list[task_number]['title']}")
        else:
            print("That number is not in the list please try again.")
    except ValueError:
        print("Please enter a number on the list.")
    
def delete_task(task_list):
    view_tasks(task_list)
    try:
        task_number = int(input("Please enter a task number to delete: "))
        if 0 <= task_number < len(task_list):
            remove_task = task_list.pop(task_number)
            print(f"task removed: {remove_task['title']}")
        else:
            print("That number is not in the list please try again.")
    except ValueError:
        print("Please enter anumber from the list.")

def main():
    task_list = []
    while True:
        menu()
        try:
            action = int(input("Please select a number (1-5): "))
            if action == 1:
                add_task(task_list)
            elif action == 2:
                view_tasks(task_list)
            elif action == 3:
                complete_task(task_list)
            elif action == 4:
                delete_task(task_list)
            elif action == 5:
                print("Quitting the To-Do List App.")
                break
            else:
                print("That option is not on the menu please try again.")
        except ValueError:
            print("Please enter a number.")


main()