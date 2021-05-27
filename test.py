import datetime

from Solution import Solution


def print_inorder(node):
    if not node:
        return
    print_inorder(node.left)
    print(node.val, end=' ')
    print_inorder(node.right)


def print_preorder(node):
    if not node:
        return
    print(node.val, end=' ')
    print_inorder(node.left)
    print_inorder(node.right)


def print_postorder(node):
    if not node:
        return
    print_inorder(node.left)
    print_inorder(node.right)
    print(node.val, end=' ')


def buildTree(list, i=0):
    node = None
    if i < len(list):
        node = TreeNode(list[i])
        node.left = buildTree(list, (2 * i) + 1)
        node.right = buildTree(list, (2 * i) + 2)
    return node


A = [1, 1, 1, 3, 3, 4, 6, 5, 3, 3]
B = 10
C = 3
sol = Solution()
s = datetime.datetime.now()
temp = sol.solve(A, B, C)
print(temp)
# print("inoder: ", end=":")
# print_inorder(temp)
# print()
# print("preorder: ", end=":")
# print_preorder(temp)
# print()
# print("postorder: ", end=":")
# print_postorder(temp)
# print()
e = datetime.datetime.now()
print(e - s)


# cook your dish here

def quickSort(arr, low, high):
    if high <= low:
        return
    
    p = partition(arr, low, high)
    
    quickSort(arr, low, p - 1)
    quickSort(arr, p + 1, high)


def partition(arr, low, high):
    pivot = high
    i = low
    for j in range(low, high):
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return i


# n = int(int(input()))
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# quickSort(arr, 0, n - 1)
# for x in arr:
#     print(x)
# a = int(input())
# print("YES" if a & 1 == 0 and a != 2 else "NO")

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
