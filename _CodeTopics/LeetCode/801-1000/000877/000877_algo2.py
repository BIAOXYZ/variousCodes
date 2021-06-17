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
        return True if dp[0][length-1] > 0 else False
        
"""
https://leetcode-cn.com/submissions/detail/187629473/

46 / 46 个通过测试用例
状态：通过
执行用时: 220 ms
内存消耗: 16.6 MB

执行用时：220 ms, 在所有 Python 提交中击败了18.20%的用户
内存消耗：16.6 MB, 在所有 Python 提交中击败了28.20%的用户
"""
