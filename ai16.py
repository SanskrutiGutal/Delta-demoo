maze = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

def heuristic(pos):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

current = start
path = [current]
visited = {current}

while current != goal:
    r, c = current
    neighbors = [
        (r + 1, c), (r - 1, c),
        (r, c + 1), (r, c - 1)
    ]

    valid = [
        (x, y) for x, y in neighbors
        if 0 <= x < len(maze)
        and 0 <= y < len(maze[0])
        and maze[x][y] == 0
        and (x, y) not in visited
    ]

    if not valid:
        print("Hill-Climbing got stuck.")
        break

    next_pos = min(valid, key=heuristic)

    if heuristic(next_pos) >= heuristic(current):
        print("No better neighbor found.")
        break

    current = next_pos
    path.append(current)
    visited.add(current)

if current == goal:
    print("Goal reached!")
print("Path:", path)