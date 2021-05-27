class Fibonacci:

    def __init__(self):
        self.memo = {}

    def get_fibonacci(self, n):
        if n < 0:
            raise Exception("Value Error")
        elif n in [0, 1]:
            return n
        if n in self.memo:
            return self.memo[n]
        result = self.get_fibonacci(n - 1) + self.get_fibonacci(n - 2)
        self.memo[n] = result
        return result


def fib(n):
    if n < 0:
        raise Exception("Value Error")
    if n in [0, 1]:
        return n

    prev_prev = 0
    prev = 1

    for _ in range(n - 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    return current


ni = Fibonacci()
print(ni.get_fibonacci(12))
print(fib(12))
