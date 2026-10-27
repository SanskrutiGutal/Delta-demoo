from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bidirectional(start, goal):
    if start == goal:
        return [start]

    q1 = deque([start])
    q2 = deque([goal])

    parent1 = {start: None}
    parent2 = {goal: None}

    while q1 and q2:
        for queue, parents, other in [
            (q1, parent1, parent2),
            (q2, parent2, parent1)
        ]:
            node = queue.popleft()

            for neighbor in graph[node]:
                if neighbor not in parents:
                    parents[neighbor] = node
                    queue.append(neighbor)

                if neighbor in other:
                    meet = neighbor

                    path1 = []
                    current = meet
                    while current is not None:
                        path1.append(current)
                        current = parent1.get(current)
                    path1.reverse()

                    path2 = []
                    current = meet
                    while current is not None:
                        current = parent2.get(current)
                        if current is not None:
                            path2.append(current)

                    return path1 + path2

    return None

print("Path:", bidirectional('A', 'F'))