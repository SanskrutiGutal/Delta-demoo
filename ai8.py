graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dls(node, goal, limit, path=None):
    if path is None:
        path = [node]

    if node == goal:
        return path

    if limit == 0:
        return None

    for neighbor in graph.get(node, []):
        if neighbor not in path:
            result = dls(
                neighbor, goal, limit - 1, path + [neighbor]
            )
            if result:
                return result

    return None

print("Path:", dls('A', 'F', 2))