class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        # trivial的两重for循环，每重循环里面挨个异或来计算肯定超时，但是还是先写下。

        def cal_matrix_xor(a, b):
            res = 0
            for i in range(a+1):
                for j in range(b+1):
                    res ^= matrix[i][j]
            return res

        m, n = len(matrix), len(matrix[0])
        vals = []
        for i in range(m):
            for j in range(n):
                vals.append(cal_matrix_xor(i, j))
        vals.sort(reverse=True)
        return vals[k-1]
        
"""
https://leetcode-cn.com/submissions/detail/178779654/

40 / 49 个通过测试用例
状态：超出时间限制
"""
