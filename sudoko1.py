def empty(su):
    for i in range(9):
        for j in range(9):
            if su[i][j] == 0:
                return i,j
    return None

def isvalid(su,val,row,col):
    for i in range(9):
        if su[row][i] == val and i != col:
            return False
    for i in range(9):
        if su[i][col] == val and i != row:
            return False
    for i in range((row//3)*3, (row//3)*3 + 3):
        for j in range((col//3)*3, (col//3)*3 + 3):
            if su[i][j] == val and (i,j) != (row,col):
                return False
    return True

def solve(su):
    if not empty(su):
        return True
    else:
        row,col = empty(su)
    for i in range(1,10):
        if isvalid(su,i,row,col):
            su[row][col] = i

            if solve(su):
                return True

            su[row][col] = 0
    return False

sudoku = [[0,1,0,0,8,9,0,0,4],[7,0,0,0,0,0,3,0,0],[0,0,0,3,0,6,5,0,1],[9,7,1,4,0,3,2,8,0],[0,6,3,5,9,2,1,4,0],[5,0,0,0,0,0,9,6,0],
[4,0,7,0,3,5,0,0,0],[0,3,8,0,0,0,4,0,0],[0,0,0,8,0,0,0,0,9]]
print(sudoku)
solve(sudoku)
print(sudoku)



