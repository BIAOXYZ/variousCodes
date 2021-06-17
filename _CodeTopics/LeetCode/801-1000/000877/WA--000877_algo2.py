class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        length = len(piles)
        dp = [[0 for i in range(length)] for j in range(length)]

        for i in range(length):
            for j in range(i, length):
                if i == j:
                    dp[i][j] = piles[i]
                elif i < j:
                    dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
                else:
                    continue
        return dp[0][length-1]
        
"""
https://leetcode-cn.com/submissions/detail/187629427/

0 / 46 个通过测试用例
状态：解答错误

最后执行的输入：
[5,3,4,5]
"""
