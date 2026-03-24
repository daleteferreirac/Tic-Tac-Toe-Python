from random import randrange

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

def showBoard(board):
    print("+--+--+--+")
    for i in range(3):
        print(board[i])
    print("+--+--+--+")

showBoard(board)

def list_of_free_spaces(board):
    freeSpaces = []
    for l, c in enumerate(board):
        for i, j in enumerate(c):
            if j == "O" or j == "X":
                pass
            else:
                freeSpaces.append(j)
    return freeSpaces

def victory_for(board, sign):
    # lines
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
        # cols
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
        # dials
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False

def enterMove(board):
    while True:
        move = input("whats your move? ")
        if not move.isdigit():
            print("enter a number")
            continue

        move = int(move)

        if move not in list_of_free_spaces(board):
            print("invalid move, try again")
            continue

        for l, c in enumerate(board):  # l-> line, c-> item
            for i, j in enumerate(c):  # i-> index, j-> value, [1, 2, 3]
                if j == move:
                    board[l][i] = "O"
                    showBoard(board)
                    return
        break
    showBoard(board)

def computerMove(board):
    print("it's computer time:")
    freeSpaces = list_of_free_spaces(board)
    i = randrange(len(freeSpaces))
    choice = freeSpaces[i]
    for l, c in enumerate(board):  # l-> line, c-> item
        for i, j in enumerate(c):  # i-> index, j-> value, [1, 2, 3]
            if j == choice:
                board[l][i] = "X"
    return showBoard(board)

while True:

    enterMove(board)

    if victory_for(board, "O"):
        print("you win")
        break

    if list_of_free_spaces(board) == []:
        print("draw")
        break


    computerMove(board)

    if victory_for(board, "X"):
        print("computer win")
        break

    if list_of_free_spaces(board) == []:
        print("draw")
        break






