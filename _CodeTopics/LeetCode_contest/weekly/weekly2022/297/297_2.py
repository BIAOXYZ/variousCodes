class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for col in range(n):
            dp[0][col] = grid[0][col]
        
        for i in range(1, m):
            for j in range(n):
                curr = float('inf')
                for k in range(n):
                    row = grid[i-1][k]
                    curr = min(curr, dp[i-1][k] + moveCost[row][j] + grid[i][j])
                dp[i][j] = curr
        return min(dp[m-1])
    
"""
https://leetcode.cn/submissions/detail/324341318/

34 / 34 个通过测试用例
状态：通过
执行用时: 344 ms
内存消耗: 16.5 MB
"""
