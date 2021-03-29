import bisect
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rows, cols = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[rows-1][cols-1]:
            return False
        
        firstColumn = [matrix[i][0] for i in range(rows)]
        rowInd = bisect.bisect_left(firstColumn, target)
        # 此时一定等于第一个元素。
        if rowInd == 0:
            return True
        
        possibleRow = matrix[rowInd-1]
        colInd = bisect.bisect_left(possibleRow, target)
        # 这行是用bisect库查找某个元素是否在列表里的经典做法。
        if colInd != cols and target == possibleRow[colInd]:
            return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/161524719/

119 / 133 个通过测试用例
状态：解答错误

输入：
[[1],[3]]
3
输出：
false
预期：
true
"""
