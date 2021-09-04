class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

       # 其实最开始的那种写法算是 “无滚动数组优化版的” 动态规划。
       # 这里写个最 plain 的动态规划吧。实际上应该先有这个，再有后面那个，不过无所谓了。

        if n < 2:
            return n
        dp = [0, 1] + [0] * (n-1)
        
        MOD = 10**9 + 7
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] % MOD
        
"""
https://leetcode-cn.com/submissions/detail/215016041/

51 / 51 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 13.4 MB

执行用时：8 ms, 在所有 Python 提交中击败了98.97%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了5.08%的用户
"""
