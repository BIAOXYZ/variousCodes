class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        for col in range(1, n):
            dp[0][col] = dp[0][col-1] + grid[0][col]
        for row in range(1, m):
            dp[row][0] = dp[row-1][0] + grid[row][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]
        
"""
https://leetcode.cn/submissions/detail/410418604/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
99.35%
的用户
内存消耗：
17.6 MB
, 在所有 Python3 提交中击败了
5.11%
的用户
通过测试用例：
61 / 61
"""
