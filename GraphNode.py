class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbours = set()
        self.colour = None


a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbours.add(b)
b.neighbours.add(a)
b.neighbours.add(c)
c.neighbours.add(b)

graph = [a, b, c]
print(graph[2].neighbours)
