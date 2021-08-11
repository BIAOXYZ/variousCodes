class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        # 这次 dp[i][j] 表示 s[i] 到 s[j] 之间可能存在的最长回文子序列，不见得必须以这俩开头or结尾。
        dp = [[1 for _ in range(length)] for _ in range(length)]
        
        res = 1
        for end in range(1, length):
            for start in range(end - 1, -1, -1):
                if s[end] != s[start]:
                    if start == end - 1:
                        dp[start][end] = 1
                    else:
                        dp[start][end] = max(dp[start][end-1], dp[start+1][end])
                else:
                    if start == end - 1:
                        dp[start][end] = 2
                    else:
                        dp[start][end] = max(dp[start][end-1], dp[start+1][end], 2 + dp[start+1][end-1])
                res = max(res, dp[start][end])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/205973822/

86 / 86 个通过测试用例
状态：通过
执行用时: 2132 ms
内存消耗: 28.5 MB

执行用时：2132 ms, 在所有 Python 提交中击败了6.51%的用户
内存消耗：28.5 MB, 在所有 Python 提交中击败了28.05%的用户
"""
