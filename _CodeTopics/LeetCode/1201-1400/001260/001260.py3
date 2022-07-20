class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        if m == n == 1:
            return grid
        
        def shift():
            lastElem = currElem = None
            for i in range(m):
                for j in range(n):
                    if i == j == 0:
                        lastElem = grid[i][j]
                        grid[i][j] = grid[m-1][n-1]
                    else:
                        currElem = grid[i][j]
                        grid[i][j] = lastElem
                        lastElem = currElem
        
        for i in range(k):
            shift()
        return grid
        
"""
https://leetcode.cn/submissions/detail/339480377/

执行用时：
324 ms
, 在所有 Python3 提交中击败了
11.79%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
99.13%
的用户
通过测试用例：
107 / 107
"""
