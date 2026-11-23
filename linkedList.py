class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

def add(self,data):
    newNode = Node(data)

    if self.head is None:
        self.head = newNode
        return

    current = self.head


    while current.next is not None:
        current = current.next

    current.next = newNode


def show(self):
    current = self.head

    if current is None:
        print("List is empty!")
        return

    while current is not None:
        print(current.data)
        current = current.next


def removeFirst(self):
    if self.head is None:
        print("List is empty!")
        return

    self.head = self.head.next