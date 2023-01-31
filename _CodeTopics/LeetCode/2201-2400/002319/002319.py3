class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:

        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i == n - 1 - j:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True
        
"""
https://leetcode.cn/submissions/detail/398229510/

执行用时：
48 ms
, 在所有 Python3 提交中击败了
78.52%
的用户
内存消耗：
15.6 MB
, 在所有 Python3 提交中击败了
79.87%
的用户
通过测试用例：
84 / 84
"""
