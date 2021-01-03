class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 其实上一个实现（`000509_algo3.py`）不那么像动态规划，或者说是滚动数组优化版的动态规划。
        # 这里写一个plain的dp吧。

        if n < 2:
            return n

        dp = [0,1] + [0 for i in range(n-1)]
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
"""
https://leetcode-cn.com/submissions/detail/135726313/

31 / 31 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.1 MB

执行用时：16 ms, 在所有 Python 提交中击败了79.31%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了12.96%的用户
"""
