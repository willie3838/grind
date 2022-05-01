'''

[1,2,3,4]
[2,4,6,8]
[3,6,9,12]

[1,2,3,4]
[x,x,x,x]
[3,6,9,12]

[x,2,3,4]
[x,x,x,x]
[x,6,9,12]

[x,x,x,x]
[x,x,x,x]
[x,6,9,12]

'''

def query(n, m, queries):
    board = []
    minn = [0,0]
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append((i+1)*(j+1))
        board.append(tmp)

    res = []
    for query in queries:
        if len(query) == 1:
            res.append(board[minn[0]][minn[1]])
        elif query[0] == 1:
            deactivateRow(query[1]-1, board, minn)
        else:
            deactivateCol(query[1]-1, board, minn)
        print(board, "\n")
    return res


def deactivateRow(row, board, minn):
    for j in range(len(board[0])):
        board[row][j] = "X"
        if row == minn[0]:
            while minn[0] < len(board)-1 and board[minn[0]][minn[1]] == "X":
                minn[0] += 1


def deactivateCol(col, board, minn):
    for i in range(len(board)):
        board[i][col] = "X"
        if col == minn[1]:
            while minn[1] < len(board[0])-1 and board[minn[0]][minn[1]] == "X":
                minn[1] += 1



print(query(3,4,[[0],[1,2],[0],[2,1], [0],[1,1],[0] ]))