class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        rows, cols = len(matrix), len(matrix[0])
        transposedMatrix = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(cols):
            for j in range(rows):
                transposedMatrix[i][j] = matrix[j][i]
        return transposedMatrix
        
"""
https://leetcode-cn.com/submissions/detail/148453055/

36 / 36 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.8 MB

执行用时：20 ms, 在所有 Python 提交中击败了99.42%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了74.66%的用户
"""
