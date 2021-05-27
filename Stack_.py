from Node import Node


class Stack_:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        temp = self.top
        self.top = temp.next
        return temp.value

    def print(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def peek(self):
        if self.top is None:
            return None
        return self.top.value

    def is_empty(self):
        if self.top is None:
            return True
        return False
