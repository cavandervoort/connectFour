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

def newMove(board,whosTurn):
    if whosTurn == 1:
        piece = "X"
    else:
        piece = "O"
    while True:
        column = input(f"Player {piece}, please choose a column (0-6): ")
        try:
            column = int(column)
        except:
            column = 99
        if column >= 0 and column <= 6:
            if board[column] != 0:
                column = 99
            if column >= 0 and column <= 6:
                break

    print(f'you selected a VALID COLUMN: {column}')
    row = 0
    while row < 5 and board[row*7 + 7 + column] == 0:
        row += 1
    pos = row * 7 + column

    return pos

def playGame():
    whosTurn = 1
    board = [0] * 42
    turnCount = 0
    while True:
        pos = newMove(board,whosTurn)
        board[pos] = whosTurn
        printBoard(board)
        if didLastMoveWinGame(board,pos,whosTurn):
            print("\nGame over, Brother!")
            return whosTurn
        whosTurn *= -1
        turnCount += 1
        if turnCount == 42:
            print("Board is full")
            return 0

def didLastMoveWinGame(board,pos,whosTurn):
    # check vertical win
    count = 0
    checkPos = pos
    while checkPos < 42:
        if board[checkPos] == whosTurn:
            count += 1
            if count == 4:
                print("\nVertical Win")
                return True
            checkPos += 7
        else:
            break

    # check horizontal win
    row = pos // 7
    for rowStart in range(row*7,row*7+4):
        if sum(board[rowStart:rowStart+4]) == 4 * whosTurn:
            print("\nHorizontal Win")
            return True

    # check diagonal up-slope win
    diagStart = pos
    while diagStart % 7 > 0 and diagStart // 7 < 5:
        diagStart += 6
    count = 0
    while diagStart >= 0:
        if board[diagStart] == whosTurn:
            count += 1
            if count == 4:
                print("\nDiagonal-Up Win")
                return True
        else:
            count = 0
        diagStart -= 6

    # check diagonal down-slope win
    diagStart = pos
    while diagStart % 7 > 0 and diagStart // 7 > 0:
        diagStart -= 8
    count = 0
    while diagStart < 42:
        if board[diagStart] == whosTurn:
            count += 1
            if count == 4:
                print("\nDiagonal-Down Win")
                return True
        else:
            count = 0
        diagStart += 8

    return False

playGame()
