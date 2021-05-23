class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        
        n = len(s)
        if s[n-1] == "1":
            return False
        dp = [True] + [False] * (n-1)
        for i in range(n):
            if s[i] == "0" and dp[i] == True:
                for j in range(minJump, min(maxJump+1, n-i)):
                    if s[i+j] == "0":
                        dp[i+j] = True
        return dp[n-1]
    
"""
https://leetcode-cn.com/submissions/detail/180022761/

107 / 123 个通过测试用例
状态：超出时间限制
"""
