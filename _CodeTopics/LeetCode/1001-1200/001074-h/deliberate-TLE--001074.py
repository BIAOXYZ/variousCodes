class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """

        # 先来个trivial的，肯定超时。

        def cal_sum_of_submatrix(x1, x2, y1, y2):
            return sum(matrix[row][col] for col in range(y1, y2 + 1) for row in range(x1, x2 + 1))
        
        res = 0
        rows, cols = len(matrix), len(matrix[0])
        for i1 in range(rows):
            for i2 in range(i1, rows):
                for j1 in range(cols):
                    for j2 in range(j1, cols):
                        if cal_sum_of_submatrix(i1, i2, j1, j2) == target:
                            res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/181802252/

35 / 40 个通过测试用例
状态：超出时间限制
"""
