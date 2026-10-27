graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

n = len(graph)

def solve_with_k_colors(k):
    colors = [0] * n

    def safe(vertex, color):
        for neighbor in range(n):
            if graph[vertex][neighbor] and colors[neighbor] == color:
                return False
        return True

    def solve(vertex):
        if vertex == n:
            return True

        for color in range(1, k + 1):
            if safe(vertex, color):
                colors[vertex] = color

                if solve(vertex + 1):
                    return True

                colors[vertex] = 0

        return False

    return colors if solve(0) else None

for k in range(1, n + 1):
    solution = solve_with_k_colors(k)

    if solution:
        print("Minimum colors:", k)
        print("Color assignment:", solution)
        break