def n_queens(n):
    board = [-1] * n
    columns = set()
    diagonal1 = set()
    diagonal2 = set()

    def solve(row):
        if row == n:
            return True

        for col in range(n):
            d1 = row - col
            d2 = row + col

            if (col not in columns
                and d1 not in diagonal1
                and d2 not in diagonal2):

                board[row] = col
                columns.add(col)
                diagonal1.add(d1)
                diagonal2.add(d2)

                if solve(row + 1):
                    return True

                columns.remove(col)
                diagonal1.remove(d1)
                diagonal2.remove(d2)
                board[row] = -1

        return False

    return board if solve(0) else None

n = 8
solution = n_queens(n)

if solution:
    for row in range(n):
        print(" ".join("Q" if solution[row] == col else "." for col in range(n)))
else:
    print("No solution exists.")