class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        N = -n if n < 0 else n
        currMultiplier, res = x, 1

        while N > 0:
            if N % 2 == 1:
                res *= currMultiplier
            N /= 2
            currMultiplier *= currMultiplier
        return 1/res if n < 0 else res
        
"""
https://leetcode-cn.com/submissions/detail/121456720/

304 / 304 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB

执行用时：16 ms, 在所有 Python 提交中击败了89.62%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了5.09%的用户
"""
