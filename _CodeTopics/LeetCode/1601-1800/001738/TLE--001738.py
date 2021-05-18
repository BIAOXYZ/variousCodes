class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        # 前缀和（异或）法，但是先是只考虑每行预计算前缀和。
        
        m, n = len(matrix), len(matrix[0])
        prefixXor = []
        for i in range(m):
            tmp = [matrix[i][0]]
            for j in range(1, n):
                tmp.append(tmp[-1] ^ matrix[i][j])
            prefixXor.append(tmp)

        def cal_matrix_xor(a, b):
            res = 0
            for i in range(a+1):
                res ^= prefixXor[i][b]
            return res

        vals = []
        for i in range(m):
            for j in range(n):
                vals.append(cal_matrix_xor(i, j))
        vals.sort(reverse=True)
        return vals[k-1]
        
"""
https://leetcode-cn.com/submissions/detail/178782895/

43 / 49 个通过测试用例
状态：超出时间限制
"""
"""
这个比前面那个 `deliberate-TLE--001738.py` 多过了3个用例，但是最终还是不行。所以一维的预计算是不够的。。。
"""
