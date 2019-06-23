class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i,j):
            #判断当前点是否合法
            if i < 0 or j < 0 or i == n or j == m: return 
            #海水部分也直接跳过
            if grid[i][j] == '0': return
            #当前位置变为海水
            grid[i][j] = '0'
            #递归四个区域
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)
        
        #如果n或者m为0，无岛屿
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        if m == 0: return 0
        
        #答案初始化为0
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    #如果grid[i][j]是岛屿，说明发现了新的岛屿
                    ans += 1
                    dfs(i,j)
        return ans
