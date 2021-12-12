class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        rowMaxVals, colMaxVals = [], []
        for i in range(n):
            rowMaxVals.append(max(grid[i]))
        for j in range(n):
            currColMax = max(grid[i][j] for i in range(n))
            colMaxVals.append(currColMax)
        
        res = 0
        for i in range(n):
            for j in range(n):
                res += min(rowMaxVals[i], colMaxVals[j]) - grid[i][j]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/247898784/

执行用时：20 ms, 在所有 Python 提交中击败了93.18%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了54.55%的用户
通过测试用例：
133 / 133
"""
