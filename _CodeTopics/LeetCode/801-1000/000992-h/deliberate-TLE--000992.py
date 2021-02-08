class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        # 应该会超时，因为for循环里没有充分利用前面子数组携带的信息。而且这好歹是个困难题，
        # 就算是 `Hard-`，应该也不至于这点代码就能写完。。。

        length = len(A)
        res = 0
        for left in range(length - K + 1):
            for right in range(left + K, length + 1):
                currSet = set(A[left:right])
                currKindOfNum = len(set(A[left:right]))
                if currKindOfNum == K:
                    res += 1
                elif currKindOfNum > K:
                    break
        return res
        
"""
https://leetcode-cn.com/submissions/detail/144821029/

42 / 55 个通过测试用例
状态：超出时间限制
"""
