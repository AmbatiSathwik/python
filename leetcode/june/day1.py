class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,i,j):
            if i<0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            nei = 1
            nei += dfs(grid,i-1,j)
            nei += dfs(grid,i+1,j)
            nei += dfs(grid,i,j-1)
            nei += dfs(grid,i,j+1)
            return nei
                        
        ma = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ma = max(ma,dfs(grid,i,j))
        return ma
    
