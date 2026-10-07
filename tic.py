from math import inf

def show(board):
    print("\n".join(" | ".join(row) for row in board))
    print()

def winner(b):
    lines = b + list(zip(*b)) + [
        [b[0][0], b[1][1], b[2][2]],
        [b[0][2], b[1][1], b[2][0]]
    ]

    for line in lines:
        if line[0] != " " and line.count(line[0]) == 3:
            return line[0]

    return None

def minimax(b, ai_turn):
    win = winner(b)

    if win == "X":
        return 1
    if win == "O":
        return -1
    if all(cell != " " for row in b for cell in row):
        return 0

    scores = []

    for r in range(3):
        for c in range(3):
            if b[r][c] == " ":
                b[r][c] = "X" if ai_turn else "O"
                scores.append(minimax(b, not ai_turn))
                b[r][c] = " "

    return max(scores) if ai_turn else min(scores)

def best_move(b):
    best_score = -inf
    move = None

    for r in range(3):
        for c in range(3):
            if b[r][c] == " ":
                b[r][c] = "X"
                score = minimax(b, False)
                b[r][c] = " "

                if score > best_score:
                    best_score = score
                    move = (r, c)

    return move

board = [[" " for _ in range(3)] for _ in range(3)]

while True:
    show(board)

    try:
        r, c = map(int, input("Enter row and column (0-2): ").split())

        if not (0 <= r < 3 and 0 <= c < 3) or board[r][c] != " ":
            print("Invalid move.")
            continue

        board[r][c] = "O"

    except ValueError:
        print("Enter two numbers, such as: 1 2")
        continue

    if winner(board) or all(cell != " " for row in board for cell in row):
        break

    r, c = best_move(board)
    board[r][c] = "X"

    if winner(board) or all(cell != " " for row in board for cell in row):
        break

show(board)

if winner(board):
    print("Winner:", winner(board))
else:
    print("It's a tie!")