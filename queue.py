taskQueue = []

def addToQueue(task):
    taskQueue.append(task)
    print("Task added to queue succesfully!")

def completeNextTask():
    if not taskQueue:
        print("Queue is empty!")
        return

    task = taskQueue.pop(0)
    print(f"Completed: {task["name"]}")


def showQueue():
    if not taskQueue:
        print("Queue is empty!")
        return

    for task in taskQueue:
        print(f"ID: {task["id"]}")
        print(f"Name: {task["name"]}")
        print(f"Status: {task["status"]}")