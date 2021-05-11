class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        # trivial的解法，应该会超时。

        res = []
        for l, r in queries:
            tmp = 0
            for i in range(l, r+1):
                tmp ^= arr[i]
            res.append(tmp)
        return res
        
"""
41 / 42 个通过测试用例
状态：超出时间限制
"""
