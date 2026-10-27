graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

n = len(graph)
colors = 3
result = [0] * n

def safe(vertex, color):
    for i in range(n):
        if graph[vertex][i] and result[i] == color:
            return False
    return True

def color_graph(vertex):
    if vertex == n:
        return True

    for color in range(1, colors + 1):
        if safe(vertex, color):
            result[vertex] = color

            if color_graph(vertex + 1):
                return True

            result[vertex] = 0

    return False

if color_graph(0):
    print("Vertex colors:", result)
else:
    print("No valid coloring found.")