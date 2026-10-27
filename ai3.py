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

player = "X"

while True:
    empty = [i for i in range(9) if board[i] == " "]

    if not empty:
        print("Match Draw!")
        break

    move = random.choice(empty)
    board[move] = player

    print("\nMove:", move + 1)
    for i in range(0, 9, 3):
        print(board[i:i+3])

    if check():
        print(player, "wins!")
        break

    player = "O" if player == "X" else "X"