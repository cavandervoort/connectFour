'''
Code by cameron.albin & christopher.vandervoort

Functions:
- printBoard - input: board - output: None
- didLastMoveWinGame - input: board,pos,whosTurn - output: boolean
- newHumanMove - input: board,whosTurn - output: column
- playGame - input: None - output: winner(int of -1 , 0, or 1)
- placePiece - input: board,whosTurn,column - output: pos

Imported Functions:
- botBuildAndRun.createBotWeights() - input: None - output: botWeights
- botBuildAndRun.runLayer - inputs: boardInput,bot - outputs: columnPreferences
'''

import botBuildAndRun

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
    return

def didLastMoveWinGame(board,pos,whosTurn):
    # check vertical win
    count = 0
    checkPos = pos
    while checkPos < 42:
        if board[checkPos] == whosTurn:
            count += 1
            if count == 4:
                return True
            checkPos += 7
        else:
            break

    # check horizontal win
    row = pos // 7
    for rowStart in range(row*7,row*7+4):
        if sum(board[rowStart:rowStart+4]) == 4 * whosTurn:
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
                return True
        else:
            count = 0
        diagStart += 8

    return False

def placePiece(board,whosTurn,column):
    row = 0
    while row < 5 and board[row*7 + 7 + column] == 0:
        row += 1
    pos = row * 7 + column

    return pos

def playGameBots(botA,botB):
    "WELCOME TO THE BOTS ONLY GAME"
    whosTurn = 1
    board = [0] * 42
    turnCount = 0
    while True:
        if whosTurn == 1:
            bot = botA
            boartToAnalyze = board
        else:
            bot = botB
            boartToAnalyze = [-1*x for x in board]

        if bot == None:
            column_list = [3,2,4,1,5,0,6]
        else:
            column_list = botBuildAndRun.runBot(boartToAnalyze,bot)
        while board[column_list[0]] != 0:
            column_list.pop(0)
        column = column_list[0]

        pos = placePiece(board,whosTurn,column)
        board[pos] = whosTurn
        if didLastMoveWinGame(board,pos,whosTurn):
            printBoard(board)
            if whosTurn == 1: piece = "X"
            else: piece = "O"
            print(f"\nGame over!\n{piece} wins")
            return whosTurn
        whosTurn *= -1
        turnCount += 1
        if turnCount == 42:
            printBoard(board)
            print("\nBoard is full--no one wins")
            return 0

for _ in range(10):
    botA = botBuildAndRun.createBotWeights()
    botB = botBuildAndRun.createBotWeights()

    print(playGameBots(botA,botB))
