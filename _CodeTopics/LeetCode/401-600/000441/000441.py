class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 1
        while n >= i:
            n -= i
            i += 1
        return i - 1
        
"""
https://leetcode-cn.com/submissions/detail/227282309/

1335 / 1335 个通过测试用例
状态：通过
执行用时: 388 ms
内存消耗: 13.1 MB

执行用时：388 ms, 在所有 Python 提交中击败了27.57%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了29.19%的用户
"""
