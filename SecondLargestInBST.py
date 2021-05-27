from BinarySearchTree import BinarySearchTree


def find_largest(node):
    if node is None:
        raise ValueError("node is None")
    if node.right:
        return find_largest(node.right)
    return node.value


def find_second_largest(node):
    if node is None or (node.right is None and node.left is None):
        raise ValueError("insufficient nodes")

    current_node = node
    while current_node:
        if current_node.left is not None and current_node.right is None:
            return find_largest(current_node.left)

        if current_node.right is not None and current_node.right.left is None and current_node.right.right is None:
            return current_node.value
        current_node = current_node.right


root = BinarySearchTree(50)
root.push(30)
root.push(80)
root.push(90)
root.push(20)
root.push(70)
root.push(40)
root.push(10)
root.push(60)
root.push(85)
root.push(100)
root.push(99)
root.push(98)
root.push(91)
root.push(92)
print(find_second_largest(root.head))
