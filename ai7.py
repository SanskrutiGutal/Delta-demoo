graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

print("Path:", dfs('A', 'F'))