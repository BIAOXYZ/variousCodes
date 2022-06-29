class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)

        # dp[i][j] 表示第一个字符串的 0 -- i 字符（均为闭区间），和第二个字符串的 0 -- j 字符，
        # 也就是 text1[:i+1]，text2[:j+1] 这两个所能形成的 LCS (Longest Common Subsequence)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = int(text1[0] == text2[0])
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] | int(text1[0] == text2[j])
                elif j == 0 and i != 0:
                    dp[i][j] = dp[i-1][j] | int(text1[i] == text2[0])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + int(text1[i] == text2[j]))
        return dp[m-1][n-1]
        
"""
https://leetcode.cn/submissions/detail/330692036/

执行用时：
528 ms
, 在所有 Python3 提交中击败了
10.69%
的用户
内存消耗：
23.5 MB
, 在所有 Python3 提交中击败了
27.93%
的用户
通过测试用例：
45 / 45
"""
