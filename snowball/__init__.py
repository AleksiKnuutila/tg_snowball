def snowball_sample(graph, node, depth, current_depth=0, visited=None):
    if visited is None:
        visited = set()

    if current_depth > depth or node in visited:
        return set()

    visited.add(node)

    outgoing_nodes = set()

    for neighbor in graph.successors(node):
        outgoing_nodes.add(neighbor)
        outgoing_nodes |= snowball_sample(graph, neighbor, depth, current_depth + 1, visited)

    return outgoing_nodes
