class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        # 感觉这代码简单得有点不可思议。。。但是目前还没发现问题

        length = len(A)
        res = 0
        for i in range(length-K+1):
            if A[i] == 0:
                for j in range(i, i+K):
                    A[j] = 1 - A[j]
                res += 1
        return res if 0 not in A else -1
        
"""
https://leetcode-cn.com/submissions/detail/146627786/

91 / 110 个通过测试用例
状态：超出时间限制
"""
