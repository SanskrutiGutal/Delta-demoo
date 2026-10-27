from collections import deque

def water_jug(cap1, cap2, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            return path

        pour12 = min(a, cap2 - b)
        pour21 = min(b, cap1 - a)

        next_states = [
            (cap1, b),
            (a, cap2),
            (0, b),
            (a, 0),
            (a - pour12, b + pour12),
            (a + pour21, b - pour21)
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    return None

print("Solution:", water_jug(4, 3, 2))