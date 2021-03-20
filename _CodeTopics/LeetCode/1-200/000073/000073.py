class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])

        def set_row_zero(rowInd):
            for i in range(cols):
                matrix[rowInd][i] = 0
        def set_col_zero(colInd):
            for row in matrix:
                row[colInd] = 0
        
        zeroRows, zeroCols = set(), set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)
        for rowInd in zeroRows:
            set_row_zero(rowInd)
        for colInd in zeroCols:
            set_col_zero(colInd)
        
"""
https://leetcode-cn.com/submissions/detail/157730168/

164 / 164 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.9 MB

执行用时：36 ms, 在所有 Python 提交中击败了48.74%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了7.55%的用户
"""
