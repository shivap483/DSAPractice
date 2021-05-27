from BinaryTreeNode import BinaryTreeNode


class BinarySearchTree(BinaryTreeNode):
    head = None

    def __init__(self, value):
        self.head = BinaryTreeNode(value)

    def push(self, value):
        temp = self.head
        while temp:
            if value > temp.value:
                if temp.right is None:
                    temp.right = BinaryTreeNode(value)
                    return
                temp = temp.right
            elif value < temp.value:
                if temp.left is None:
                    temp.left = BinaryTreeNode(value)
                    return
                temp = temp.left
            elif value == temp.value:
                print(value, "is already present in tree")
                return
        return self.head


def is_valid_bst_bfs(root_node):
    if not root_node:
        return True
    queue = []
    temp = root_node
    queue.append(temp)
    while len(queue):
        node = queue[0]
        print(node.value)
        del queue[0]
        if node.left:
            if node.value < node.left.value:
                return False
            queue.append(node.left)
        if node.right:
            if node.value > node.right.value:
                return False
            queue.append(node.right)
    return True


def is_valid_bst_dfs(root_node):
    if not root_node:
        return True
    temp = root_node.value
    print(temp)
    if root_node.right:
        if root_node.value > root_node.right.value:
            return False
        else:
            is_valid_bst_dfs(root_node.right)
    if root_node.left:
        if root_node.value < root_node.left.value:
            return False
        else:
            is_valid_bst_dfs(root_node.left)
    return True


def is_valid_bst(root_node):
    node_and_bound_stack = [(root_node, -float('inf'), float('inf'))]
    while len(node_and_bound_stack):
        node, lower_bound, upper_bound = node_and_bound_stack.pop()
        if node.value <= lower_bound or node.value >= upper_bound:
            return False
        if node.left:
            node_and_bound_stack.append(node.left, lower_bound, node.value)

        if node.right:
            node_and_bound_stack.append(node.right, node.value, upper_bound)

    return True

# root = BinarySearchTree(50)
# root.push(30)
# root.push(80)
# root.push(90)
# root.push(20)
# root.push(70)
# root.push(40)
# root.push(10)
# root.push(60)
# root.push(85)
# root.push(100)

# print(is_valid_bst_bfs(root.head))
# print(is_valid_bst_dfs(root.head))
