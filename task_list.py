tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# 1. Print a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_tasks = []
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    
    return uncompleted_tasks



# 2. Print a list of completed tasks
def get_completed_tasks(task_list):
    for task in task_list:
        if task["completed"] == True:
            print(task["description"])



# 3. Print a list of all task descriptions

def all_tasks(task_list):
    for task in task_list:
        print(task["description"])



# 4. Print a list of tasks where time_taken is at least a given time

def get_tasks_taking_longer_than(list, time):
    found_tasks = []
    for task in list:
        if task["time_taken"] >= time:
            found_tasks.append(task)
    
    return found_tasks

print(get_tasks_taking_longer_than(tasks, 30))

# 5. Print any task with a given description

def print_task(description):
    for task in tasks:
        if description == task["description"]:
            return task

### Extension

# 6. Given a description update that task to mark it as complete.


def get_task_as_completed(list, description):
    for task in list:
        if description == task["description"]:
            task["completed"] = True


# 7. Add a task to the list

def add_tasks(list, task_description):
    list.append({"description": task_description})
