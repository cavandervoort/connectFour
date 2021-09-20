def printBoard(board):
    for row in range(6):
        output = "| "
        for col in range(7):
            pos = row * 7 + col
            piece = board[pos]
            if piece < 0:
                output += "O "
            elif piece > 0:
                output += "X "
            else:
                output += "  "
            output += "| "
        print(output)
    print("-"*29)
    print("")

new_board = [0] * 21 + [-1] * 11 + [1] * 10

printBoard(new_board)
