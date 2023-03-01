class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        def get_local_max(i, j):
            return max([grid[x][y] for x in range(i, i+3) for y in range(j, j+3)])
        
        n = len(grid)
        res = [[[-1] for _ in range(n-2)] for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                res[i][j] = get_local_max(i, j)
        return res
        
"""
https://leetcode.cn/submissions/detail/407604145/

执行用时：
96 ms
, 在所有 Python3 提交中击败了
54.97%
的用户
内存消耗：
16.2 MB
, 在所有 Python3 提交中击败了
5.26%
的用户
通过测试用例：
50 / 50
"""
