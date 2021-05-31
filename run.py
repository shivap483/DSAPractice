from datetime import datetime

from Solution import Solution

A = "bananas"
B = [
    [10, -8, -9, 4, 9, 3, 4],
    [-7, 1, 9, 1, -7, 9, 7],
    [-3, 10, 1, 6, -6, 7, -6],
    [-10, 5, 7, 3, -5, -4, -1],
    [6, 4, 8, 2, 1, -5, -4],
    [-10, -8, -10, -3, -1, -6, -5]
]
C = 8
test = Solution()
s = datetime.now()
print(test.minCut(A))
e = datetime.now()
print(e - s)
exit()
