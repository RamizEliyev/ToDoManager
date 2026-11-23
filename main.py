from menu import *
from queue import addToQueue,showQueue,completeNextTask
from stack import *
from tasks import *
from linkedList import * 

taskHistory = linkedList()

while True:
    showMenu()
    choice = input("Enter Your Choice:")

    if choice == "1":
        name = input("Enter Task Name:")
        addTask(name)

    elif choice == "2":
        taskID = int(input("Enter task ID:"))
        taskName = input("Enter task name:")
        updateTask(taskID,taskName)

    elif choice == "3":
        taskID = int(input("Enter task ID:"))
        removeTask(taskID)

    elif choice == "4":
        showTasks()

    elif choice == "5":
        taskID = int(input("Enter task ID:"))

        task = findTask(taskID)

        if task:
            addToQueue(task)

        else:
            print("Task not found!")

    elif choice == "6":
        completeNextTask()

    elif choice == "7":
        undo(tasks)

    elif choice == "8":
        taskHistory.show()

    elif choice == "9":
        showQueue()

    elif choice == "0":
        print("Program closed!")
        break

    else:
        print("INVALID CHOICE!")