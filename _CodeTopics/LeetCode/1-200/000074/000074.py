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
        # 这里是处理target可能和每一行的第一个元素相等的情况，之前错的那个版本没完全考虑到这点。
        if rowInd < rows and target == matrix[rowInd][0]:
            return True
        
        possibleRow = matrix[rowInd-1]
        colInd = bisect.bisect_left(possibleRow, target)
        # 这行是用bisect库查找某个元素是否在列表里的经典做法。
        if colInd != cols and target == possibleRow[colInd]:
            return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/161525988/

133 / 133 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.2 MB

执行用时：28 ms, 在所有 Python 提交中击败了13.12%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了38.65%的用户
"""
