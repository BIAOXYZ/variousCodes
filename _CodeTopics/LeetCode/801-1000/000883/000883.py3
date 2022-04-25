class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        n = len(grid)
        res = n**2 - sum(1 for i in range(n) for j in range(n) if grid[i][j] == 0)
        for row in grid:
            res += max(row)
        for col in [[grid[i][j] for i in range(n)] for j in range(n)]:
            res += max(col)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/305487730/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
80.23%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
17.11%
的用户
通过测试用例：
90 / 90
"""
