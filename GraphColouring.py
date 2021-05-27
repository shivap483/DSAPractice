def colour_graph(graph, colours):
    for node in graph:
        if node in node.neighbours:
            raise Exception("loop detected")
        illegal_colours = set([neighbour.colour for neighbour in node.neighbours if neighbour.colour])

        # legal_colours = set([colour for colour in colours if colour not in illegal_colours])
        # node.colour = legal_colours[0]
        for colour in colours:
            if colour not in illegal_colours:
                node.colour = colour
                break
