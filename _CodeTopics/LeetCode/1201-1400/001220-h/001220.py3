class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        # 'a', 'e', 'i', 'o', 'u' 分别对应 0，1，2，3，4
        MOD = 10**9 + 7
        dp = [[0 for _ in range(5)] for _ in range(n+1)]
        for i in range(5):
            dp[1][i] = 1
        
        for i in range(2, n+1):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
            dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4]) % MOD
            dp[i][3] = (dp[i-1][2] + dp[i-1][4]) % MOD
            dp[i][4] = dp[i-1][0]
        return sum(dp[n]) % MOD
        
"""
https://leetcode-cn.com/submissions/detail/259232077/

执行用时：232 ms, 在所有 Python3 提交中击败了34.85%的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了45.45%的用户
通过测试用例：
43 / 43
"""
