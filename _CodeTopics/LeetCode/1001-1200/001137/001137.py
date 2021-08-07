class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0, 1, 1]
        if n <= 2:
            return dp[n]
        
        dp += [0] * (n+1-3)
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
        
"""
https://leetcode-cn.com/submissions/detail/204436924/

39 / 39 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.2 MB

执行用时：16 ms, 在所有 Python 提交中击败了71.82%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了7.86%的用户
"""
