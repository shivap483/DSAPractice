from Stack_ import Stack_


class MaxStack:
    def __init__(self):
        self.stack = Stack_()
        self.maxes_stack = Stack_()

    def push(self, value):
        self.stack.push(value)
        if self.maxes_stack.peek() is None or self.maxes_stack.peek() <= value:
            self.maxes_stack.push(value)

    def pop(self):
        temp = self.stack.pop()
        if self.maxes_stack.peek() == temp:
            self.maxes_stack.pop()
        return temp

    def get_max(self):
        return self.maxes_stack.peek()


input = [1, 2, 3, 4, 5, 6]
inpu = [6, 5, 4, 3, 2, 1]
