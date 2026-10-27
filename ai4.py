import random

board = [" "] * 9
wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def check():
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

while True:
    print("\nBoard positions:")
    print("1 2 3\n4 5 6\n7 8 9")

    try:
        move = int(input("Enter your position (1-9): ")) - 1
        if move not in range(9) or board[move] != " ":
            print("Invalid move! Try again.")
            continue
    except ValueError:
        print("Enter a valid number.")
        continue

    board[move] = "X"

    for i in range(0, 9, 3):
        print(board[i:i+3])

    if check():
        print("Human wins!")
        break

    empty = [i for i in range(9) if board[i] == " "]
    if not empty:
        print("Match Draw!")
        break

    move = random.choice(empty)
    board[move] = "O"
    print("Computer selected:", move + 1)

    for i in range(0, 9, 3):
        print(board[i:i+3])

    if check():
        print("Computer wins!")
        break

    if " " not in board:
        print("Match Draw!")
        break
    