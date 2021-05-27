from Stack_ import Stack_


class QueueUsingStack:
    def __init__(self):
        self.s1 = Stack_()
        self.s2 = Stack_()

    def enqueue(self, value):
        self.s1.push(value)

    def dequeue(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        if self.s2.is_empty():
            print("Empty queue")
            return
        print("Popped element is ", self.s2.pop())


q: QueueUsingStack = QueueUsingStack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.enqueue(4)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.dequeue()
