class Solution:
    r = 0
    def totalNQueens(self, n: int) -> int:
        def isValid(li,row,col):
            for i in range(row):
                if li[i][col] == 1:
                    return False
            for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
                if li[i][j] == 1:
                    return False
            for i,j in zip(range(row,-1,-1),range(col,n,1)):
                if li[i][j] == 1:
                    return False
            return True
        
        def solve(li,row):
            if row >= n:
                self.r += 1
                return True
            fal = False
            for i in range(n):
                if isValid(li,row,i):
                    li[row][i] = 1
                    fal = solve(li,row+1)
                    li[row][i] = 0
            return fal
        self.r = 0
        li = [[0 for i in range(n)]for j in range(n)]
        solve(li,0)
        return self.r
