class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        smaller, larger = 0, 1
        if n == 0: return smaller
        if n == 1: return larger

        MOD = 10**9 + 7
        for i in range(2, n+1):
            smaller, larger = larger, smaller + larger
        return larger % MOD
        
"""
https://leetcode-cn.com/submissions/detail/215012601/

51 / 51 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.3 MB

执行用时：16 ms, 在所有 Python 提交中击败了69.98%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了5.08%的用户
"""
