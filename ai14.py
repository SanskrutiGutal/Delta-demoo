import random

N = 8

def heuristic(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:
                conflicts += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts

def hill_climbing():
    board = [random.randrange(N) for _ in range(N)]

    while True:
        current = heuristic(board)

        if current == 0:
            return board

        best_board = board
        best_score = current

        for col in range(N):
            for row in range(N):
                new_board = board.copy()
                new_board[col] = row
                score = heuristic(new_board)

                if score < best_score:
                    best_score = score
                    best_board = new_board

        if best_score >= current:
            board = [random.randrange(N) for _ in range(N)]
        else:
            board = best_board

solution = hill_climbing()

print("Queen positions:", solution)
print("Attacking pairs:", heuristic(solution))

for row in range(N):
    print(" ".join("Q" if solution[col] == row else "." for col in range(N)))