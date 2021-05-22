class Solution:
    r = []
    def solveNQueens(self, n: int) -> List[List[str]]:
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
                mid = []
                for i in range(n):
                    k = ''
                    for j in range(n):
                        if li[i][j] == 1:
                            k += 'Q'
                        else:
                            k += '.'
                    mid.append(k)
                self.r.append(mid)
                return True
            res = False
            for i in range(n):
                if isValid(li,row,i):
                    li[row][i] = 1
                    res = solve(li,row+1) or res
                    li[row][i] = 0
            return res
        self.r.clear()
        li = [[0 for i in range(n)]for j in range(n)]
        solve(li,0)
        return self.r
        
