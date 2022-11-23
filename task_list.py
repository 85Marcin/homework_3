tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# 1. Print a list of uncompleted tasks
def uncompleted_tasks(task_list):
    for task in task_list:
        if task["completed"] == False:
            print(task["description"])



# 2. Print a list of completed tasks
def completed_tasks(task_list):
    for task in task_list:
        if task["completed"] == True:
            print(task["description"])



# 3. Print a list of all task descriptions

def all_tasks(task_list):
    for task in task_list:
        print(task["description"])



# 4. Print a list of tasks where time_taken is at least a given time

def tasks_time_taken(task_list):
    for task in task_list:
        if task["time_taken"] >= 15:
            print(task["description"])



# 5. Print any task with a given description

def print_task(description):
    for task in tasks:
        if description == task["description"]:
            print(task)

### Extension

# 6. Given a description update that task to mark it as complete.

def update_task(description):
    for task in tasks:
        if description == task["description"]:
            task["completed"] = True

# 7. Add a task to the list

def add_task(task):
    tasks.append({"description": task})
