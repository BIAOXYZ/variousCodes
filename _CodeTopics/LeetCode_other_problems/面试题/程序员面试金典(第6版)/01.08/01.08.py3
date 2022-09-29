class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return

        def set_row_to_all_zero(i):
            for j in range(n):
                matrix[i][j] = 0
        def set_col_to_all_zero(j):
            for i in range(m):
                matrix[i][j] = 0
        
        seRow, seCol = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    seRow.add(i)
                    seCol.add(j)

        for i in seRow:
            set_row_to_all_zero(i)
        for j in seCol:
            set_col_to_all_zero(j)
        return
        
"""
https://leetcode.cn/submissions/detail/368640667/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
87.14%
的用户
内存消耗：
15.4 MB
, 在所有 Python3 提交中击败了
59.73%
的用户
通过测试用例：
159 / 159
"""
