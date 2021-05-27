from Node import Node


class Queue_:
    def __init__(self):
        self.first = self.last = None

    def enqueue(self, value):
        node = Node(value)
        if self.first is None:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node

    def dequeue(self):
        print(self.peek())
        if self.first is None:
            raise Exception("ValueError")
        if self.first == self.last:
            temp = self.first
            self.first = self.last = None
            return temp.value
        temp = self.first
        self.first = temp.next
        return temp.value

    def peek(self):
        return self.first.value

    def print(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
