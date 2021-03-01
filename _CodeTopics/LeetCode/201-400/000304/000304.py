class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        rows, cols = len(matrix), len(matrix[0])
        self.prefixSumMatrix = []
        for i in range(rows):
            l = [matrix[i][0]]
            for j in range(1, cols):
                l.append(l[-1] + matrix[i][j])
            self.prefixSumMatrix.append(l)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(row1, row2+1):
            if col1 != 0:
                res += self.prefixSumMatrix[i][col2] - self.prefixSumMatrix[i][col1-1]
            else:
                res += self.prefixSumMatrix[i][col2]
        return res
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

"""
https://leetcode-cn.com/submissions/detail/149997348/

12 / 12 个通过测试用例
状态：通过
执行用时: 244 ms
内存消耗: 15.8 MB

执行用时：244 ms, 在所有 Python 提交中击败了23.08%的用户
内存消耗：15.8 MB, 在所有 Python 提交中击败了84.62%的用户
"""
