class Solution(object):
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int
        """
        
        n = len(pressedKeys)
        dp = [0] * n
        dp[0] = 1
        MOD = 10**9+7
        
        for i in range(1, n):
            dp[i] = dp[i-1]
            if pressedKeys[i] == pressedKeys[i-1]:
                if i >= 2:
                    dp[i] += dp[i-2]
                    dp[i] %= MOD
                    if pressedKeys[i] == pressedKeys[i-2]:
                        if i >= 3:
                            dp[i] += dp[i-3]
                            dp[i] %= MOD
                            if pressedKeys[i] == pressedKeys[i-3] and pressedKeys[i] in '79':
                                if i >= 4:
                                    dp[i] += dp[i-4]
                                    dp[i] %= MOD
                                else:
                                    dp[i] += 1
                        else:
                            dp[i] += 1
                else:
                    dp[i] += 1
        return dp[n-1]
    
"""
https://leetcode-cn.com/submissions/detail/310709168/

107 / 107 个通过测试用例
状态：通过
执行用时: 376 ms
内存消耗: 20.4 MB
"""
