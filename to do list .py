tasks = []

def add_task(task):
    tasks.append(task)
    print(f"task '{task}' has been added to the list ")
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"task '{task}' has been removed from the list")
    else :
        print(f"task '{task}' not found in the list")
def show_tasks():
    if tasks:
        print("tasks in To-Do List :")
        for idx, task in enumerate(tasks, start=1):
            print (f"{idx} .{task}")
    else :
        print ("the To-Do List is empty")

while True :
    print ("\n To-Do List App Menu :")
    print ("1. Add a task")
    print ("2. Remove a task")
    print ("3. Show tasks")
    print ("4. Quit")
    choice = input("enter your choice (1/2/3/4) :")

    if choice =='1':
        task = input("enter the task to Add :")
        add_task(task)
    elif choice =='2':
        task = input("enter the task to Remove :")
        remove_task(task)
    elif choice =='3':
        show_tasks()
    elif choice =='4':
        print ("goodbye!")
        break
    else:
        print ("invalid choice . please choose a valid option")