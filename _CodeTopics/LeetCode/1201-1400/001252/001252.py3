class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:

        matrix = [[0] * n for _ in range(m)]
        for row, col in indices:
            for i in range(m):
                matrix[i][col] += 1
            for j in range(n):
                matrix[row][j] += 1
        return sum(matrix[i][j] & 1 == 1 for i in range(m) for j in range(n))
        
"""
https://leetcode.cn/submissions/detail/336030636/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
46.41%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
50.72%
的用户
通过测试用例：
44 / 44
"""
