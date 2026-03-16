from random import randrange

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

def showBoard(board):
    print("+--+--+--+")
    for i in range(3):
        print(board[i])
    print("+--+--+--+")

showBoard(board)

def enterMove(board):
    move = int(input("whats your move? "))
    if move not in list_of_free_spaces(board):
        print("invalid move, try again")
        return enterMove(board)
    else:
        for l, c in enumerate(board):  # l-> line, c-> item
            for i, j in enumerate(c):  # i-> index, j-> value, [1, 2, 3]
                if j == move:
                    board[l][i] = "O"
    return showBoard(board)

enterMove(board)



