class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        """
        :type nextVisit: List[int]
        :rtype: int
        """
        
        MOD = 10**9 + 7
        n = len(nextVisit)
        dp = [0, 2] + [0] * (n-2)
        for i in range(2, n):
            dp[i] = dp[i-1] + 2**(i - nextVisit[i-1])
        return dp[n-1] % MOD
    
"""
https://leetcode-cn.com/submissions/detail/215354417/

10 / 239 个通过测试用例
状态：解答错误

最后执行的输入：
[0,1,1,2,2,0,4,0,8]
输入：
[0,1,1,2,2,0,4,0,8]
输出：
348
预期：
194
"""
