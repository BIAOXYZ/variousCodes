class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        # dp 为二维数组，其中 dp[i][0] 表示：
        # “达成从开头到第i个位置之间的（包括第 i 个位置），以 0 结尾的子串需要的最小翻转次数。”
        # 那么 dp[i][1] 则表示 “达成从开头到第i个位置之间的，以 1 结尾的子串需要的最小翻转次数。”

        n = len(s)
        dp = [[-1, -1] for i in range(n)]
        if s[0] == '0':
            dp[0][0] = 0
            dp[0][1] = 1
        else:
            dp[0][0] = 1
            dp[0][1] = 0

        for i in range(1, n):
            ch = s[i]
            if ch == '0':
                dp[i][0] = dp[i-1][0]
                dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = min(dp[i-1][0], dp[i-1][1])
        return min(dp[n-1])
        
"""
https://leetcode.cn/submissions/detail/323968405/

执行用时：
464 ms
, 在所有 Python3 提交中击败了
25.85%
的用户
内存消耗：
26.5 MB
, 在所有 Python3 提交中击败了
14.29%
的用户
通过测试用例：
93 / 93
"""
