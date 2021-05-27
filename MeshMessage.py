from collections import deque


def get_shortest_path(graph, sender, receiver):
    if sender not in graph:
        raise Exception(sender, " not in network")
    if receiver not in graph:
        raise Exception(receiver, " not in network")
    nodes_to_visit = deque()
    nodes_to_visit.append(sender)
    how_we_reached_nodes = {sender: None}
    while len(nodes_to_visit):
        current_node = nodes_to_visit.popleft()

        if current_node is receiver:
            path = []
            while current_node:
                path.append(current_node)
                current_node = how_we_reached_nodes[current_node]
            path.reverse()
            return path

        for neighbour in graph[current_node]:
            if neighbour not in how_we_reached_nodes:
                nodes_to_visit.append(neighbour)
                how_we_reached_nodes[neighbour] = current_node

    return None


network = {
    'Min': ['William', 'Jayden', 'Omar'],
    'William': ['Min', 'Noam'],
    'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren': ['Jayden', 'Omar'],
    'Amelia': ['Jayden', 'Adam', 'Miguel'],
    'Adam': ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel': ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam': ['Nathan', 'Jayden', 'William'],
    'Omar': ['Ren', 'Min', 'Scott'],
}
print(get_shortest_path(network, 'Jayden', 'Adam'))
