from Node import Node


def kth_to_last_node(k, head):
    if k < 1:
        raise Exception("ValueError")
    current_node = head
    length = 0
    while current_node:
        current_node = current_node.next
        length += 1
    if k > length:
        raise Exception("k is greater than linked list")
    how_far = length - k
    print(how_far)
    current_node = head
    for _ in range(how_far):
        current_node = current_node.next
    print(current_node.value)


def kth_to_last_node_second_approach(k, head):
    if k < 1:
        raise Exception("ValueError")
    right_node = head
    left_node = head
    for _ in range(k - 1):
        if not right_node.next:
            raise Exception("k is greater than linked list")
        right_node = right_node.next
    while right_node.next:
        right_node = right_node.next
        left_node = left_node.next
    print(left_node.value)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
kth_to_last_node(1, a)
kth_to_last_node_second_approach(1, a)
