class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if matrix == []:
            return []
        
        res = []
        rows, columns = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                res.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    res.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    res.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res
        
"""
# https://leetcode-cn.com/submissions/detail/76625113/

27 / 27 个通过测试用例
	状态：通过
执行用时：20 ms
内存消耗：13.3 MB
"""
