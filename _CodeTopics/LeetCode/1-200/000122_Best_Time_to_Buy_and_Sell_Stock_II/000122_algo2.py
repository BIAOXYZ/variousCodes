class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        length = len(prices)
        if length <= 1:
            return 0
        
        # dp[i][0]表示第i天（交易完成后）手里没有股票时的最大利润；
        # dp[i][1]表示第i天（交易完成后）手里有股票时的最大利润。
        dp = [[0 for i in range(2)] for j in range(length)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[length-1][0]
        
"""
https://leetcode-cn.com/submissions/detail/131702070/

200 / 200 个通过测试用例
状态：通过
执行用时: 60 ms
内存消耗: 17.7 MB

执行用时：60 ms, 在所有 Python 提交中击败了21.03%的用户
内存消耗：17.7 MB, 在所有 Python 提交中击败了5.06%的用户
"""
