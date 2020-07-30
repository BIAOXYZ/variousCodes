class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 最开始想的是一维dp，初一想觉得好像不行，然后想到二维dp：每个格子dp[i][j]表示
        ## 整数i被拆分成j个数的和时，这j个数对应的乘积。但是会有很多废格子，而且最优子结构
        ## 这点似乎也不符合。
        # 最后发现想复杂了，一维dp就够了。至于数学方法，没有深入去想。因为这题看着就是dp了。

        dp = [0 for _ in range(n+1)]
        for i in range(2, n+1):
            for j in range(1, i):
                # 这里每一个j的这一轮循环里，还得和已有的dp[i]比一下。
                dp[i] = max(j*dp[i-j], j*(i-j), dp[i])
        return dp[n]
        
"""
https://leetcode-cn.com/submissions/detail/93069855/

50 / 50 个通过测试用例
状态：通过
执行用时：20 ms
内存消耗：12.8 MB
"""
"""
执行用时：20 ms, 在所有 Python 提交中击败了70.39%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了16.67%的用户
"""
