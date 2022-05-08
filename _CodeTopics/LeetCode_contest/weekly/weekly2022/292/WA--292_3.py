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
            if pressedKeys[i] != pressedKeys[i-1]:
                continue
            else:
                if i >= 2:
                    dp[i] += dp[i-2]
                    dp[i] %= MOD
                    if pressedKeys[i] != pressedKeys[i-2]:
                        continue
                    else:
                        if i >= 3:
                            dp[i] += dp[i-3]
                            dp[i] %= MOD
                            if pressedKeys[i] != pressedKeys[i-3] or pressedKeys[i] != '9':
                                continue
                            else:
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
https://leetcode-cn.com/submissions/detail/310699965/

53 / 107 个通过测试用例
状态：解答错误

输入：
"55555555999977779555"
输出：
18144
预期：
20736
"""
"""
注：其实这个也算低级失误，因为数字 7 也是能对应四个字母的，但是只考虑了数字 9。
但是还是记录一下是因为下一个版本 if-else 分支的条件都反过来了，更简洁了。
"""
