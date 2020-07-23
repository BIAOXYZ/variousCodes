class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # 这个应该算是走格子类的动态规划题目里最经典的了吧？
        # 先用最plain的二维的动态规划，后面再写有滚动数组的一维的优化。
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        dp = [[0 for i in range(cols)] for j in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0: dp[i][j] = grid[0][0]
                elif i == 0: dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0: dp[i][j] = dp[i-1][j] + grid[i][j]
                else: dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[rows-1][cols-1]
        
"""
https://leetcode-cn.com/submissions/detail/90773809/

61 / 61 个通过测试用例
状态：通过
执行用时：36 ms
内存消耗：13.9 MB
"""
"""
执行用时：36 ms, 在所有 Python 提交中击败了51.03%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了11.11%的用户
"""
