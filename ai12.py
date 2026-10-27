from collections import deque

# State: (position, room_A, room_B)
# 0 = Dirty, 1 = Clean

def vacuum_bfs():
    start = ('A', 0, 0)
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, actions = queue.popleft()
        pos, a, b = state

        if a == 1 and b == 1:
            return actions

        next_states = []

        if pos == 'A':
            next_states.append(
                (('A', 1, b), 'Clean A') if a == 0
                else (('B', a, b), 'Move Right')
            )
        else:
            next_states.append(
                (('B', a, 1), 'Clean B') if b == 0
                else (('A', a, b), 'Move Left')
            )

        for new_state, action in next_states:
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, actions + [action]))

    return None

print("Actions:", vacuum_bfs())