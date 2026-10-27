import random

board = [" "] * 9

def display():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("------")

def winner():
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in lines:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

player = "X"

while " " in board:
    move = random.choice([i for i in range(9) if board[i] == " "])
    board[move] = player
    print("\nPlayer", player, "selected position", move + 1)
    display()

    if winner():
        print(player, "wins!")
        break

    player = "O" if player == "X" else "X"
else:
    print("Match Draw!")