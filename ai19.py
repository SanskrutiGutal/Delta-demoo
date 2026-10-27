def solve_n_queens(n):
    board = [-1] * n

    def safe(row, col):
        for r in range(row):
            if board[r] == col:
                return False

            if abs(board[r] - col) == abs(r - row):
                return False

        return True

    def solve(row):
        if row == n:
            return True

        for col in range(n):
            if safe(row, col):
                board[row] = col

                if solve(row + 1):
                    return True

                board[row] = -1

        return False

    if solve(0):
        return board

    return None

n = 8
solution = solve_n_queens(n)

if solution:
    for row in range(n):
        print(" ".join("Q" if solution[row] == col else "." for col in range(n)))
else:
    print("No solution exists.")