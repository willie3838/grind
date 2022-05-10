
# TC: O(n!)
# SC: O(nxn)
# this is because of the loop that's being called recursively
def generateNQueens(n):
    board = [[0]*n for _ in range(n)]
    res = []
    generate(board, res, 0, 0)
    return res

# omitted row check bc we account for that already
def checkValid(board, row, col):    
    # cols
    for i in range(len(board)):
        if board[i][col] == "Q":
            return False

    # top left- bottom right diagonal
    x = row
    y = col

    while x >= 0 and y >= 0:
        if board[x][y] == "Q":
            return False
        x -= 1
        y -= 1
    
    x = row
    y = col

    while x < len(board) and y < len(board[0]):
        if board[x][y] == "Q":
            return False
        x += 1
        y += 1
    
    # top right - bottom left diagonal
    x = row
    y = col

    while x >= 0 and y < len(board[0]):
        if board[x][y] == "Q":
            return False
        x -= 1
        y += 1
    
    x = row
    y = col

    while x < len(board) and y >= 0:
        if board[x][y] == "Q":
            return False
        x += 1
        y -= 1
    
    return True
    

import copy
def generate(board, res, row, col):
    if row == len(board):
        res.append(copy.deepcopy(board))
        return
    for j in range(len(board[0])):
        if board[row][j] == 0:
            if checkValid(board, row, j):
                board[row][j] = "Q"
                generate(board, res, row+1, col)
                board[row][j] = 0

print(generateNQueens(4))