from BinaryTreeNode import BinaryTreeNode


def is_balanced(root_node):
    if root_node is None:
        return True

    depths = []
    nodes = []
    nodes.append((root_node, 0))
    while len(nodes):
        node, depth = nodes.pop()
        if not node.left and not node.right:
            if depth not in depths:
                depths.append(depth)

            if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                return False

        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))
    return True


root = BinaryTreeNode(0)
root.insert_left(1)
root.insert_right(2)
temp: BinaryTreeNode = root.left
temp.insert_left(3)
temp.insert_right(4)
temp = root.right
temp.insert_left(5)
temp.insert_right(6)
temp.left.insert_left(8)
temp.left.left.insert_right(9)
print(is_balanced(root))
