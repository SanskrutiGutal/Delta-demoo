graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dls(node, goal, limit, path):
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

def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls(start, goal, depth, [start])
        if result:
            return result
    return None

print("Path:", iddfs('A', 'F', 5))