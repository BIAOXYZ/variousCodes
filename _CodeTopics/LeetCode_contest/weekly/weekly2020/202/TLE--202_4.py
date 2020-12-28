class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        dp = [0 for i in range(n+1)]
        dp[1], dp[2] = 1, 2
        for i in range(3,n+1):
            if i % 2 != 0 and i % 3 != 0:
                dp[i] = 1 + dp[i-1]
            elif i % 2 != 0 and i % 3 == 0:
                dp[i] = min(1 + dp[i-1], 1 + dp[i/3])
            elif i % 2 == 0 and i % 3 != 0:
                dp[i] = min(1 + dp[i-1], 1 + dp[i/2])
            else:
                dp[i] = min(1 + dp[i-1], 1 + dp[i/2], 1 + dp[i/3])
        return dp[n]
    
"""
https://leetcode-cn.com/submissions/detail/98550860/

98 / 176 个通过测试用例
状态：超出时间限制

最后执行的输入：
9459568
"""
