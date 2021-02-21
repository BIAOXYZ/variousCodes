class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        rows, cols = len(matrix), len(matrix[0])
        for col in range(cols):
            row = 0
            constElem = matrix[0][col]
            while row < rows and col < cols:
                if matrix[row][col] != constElem:
                    return False
                row += 1; col += 1
        for row in range(1, rows):
            col = 0
            constElem = matrix[row][0]
            while row < rows and col < cols:
                if matrix[row][col] != constElem:
                    return False
                row += 1; col += 1
        return True
        
"""
https://leetcode-cn.com/submissions/detail/147498760/

483 / 483 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.8 MB

执行用时：24 ms, 在所有 Python 提交中击败了76.29%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了94.85%的用户
"""
