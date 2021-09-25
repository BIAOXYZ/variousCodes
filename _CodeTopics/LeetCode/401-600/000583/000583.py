class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        # 猜测这题应该是反向思考：先不考虑删除，而是考虑从0长度开始取，
        # 何时取到公共最长，那么用word1和word2的长度减去公共最长即可。
        # 那么到这里就发现其实也不用考虑从0开始取，实质就是求两个的公共最长子序列。

        len1, len2 = len(word1), len(word2)
        dp = [[-1 for col in range(len2)] for row in range(len1)]
        
        for row in range(len1):
            for col in range(len2):
                if row == col == 0:
                    dp[row][col] = 1 if word1[0] == word2[0] else 0
                elif row == 0 and col > 0:
                    dp[row][col] = max(dp[row][col-1], int(word1[0] == word2[col]))
                elif row > 0 and col == 0:
                    dp[row][col] = max(dp[row-1][col], int(word1[row] == word2[0]))
                elif row > 0 and col > 0:
                    dp[row][col] = max(
                        dp[row][col-1],
                        dp[row-1][col],
                        dp[row-1][col-1] + 1 if word1[row] == word2[col] else dp[row-1][col-1]
                    )
        return len1 - dp[len1-1][len2-1] + len2 - dp[len1-1][len2-1]
        
"""
https://leetcode-cn.com/submissions/detail/223132897/

1306 / 1306 个通过测试用例
状态：通过
执行用时: 264 ms
内存消耗: 15.2 MB

执行用时：264 ms, 在所有 Python 提交中击败了11.30%的用户
内存消耗：15.2 MB, 在所有 Python 提交中击败了65.65%的用户
"""
