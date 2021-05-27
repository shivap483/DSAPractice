from Node import Node


def reverse(head):
    current_node = head
    previous_node = None
    next_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node


def print_(node):
    temp = node
    while temp:
        print(temp.value)
        temp = temp.next


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
print_(a)

print_(reverse(a))
