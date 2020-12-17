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
        # 由于这两个状态只需要前一天（第 i-1 天）的就行，所以可以压缩为只需要两个变量去存即可。
        dp0 = 0
        dp1 = -prices[0]

        for i in range(1, length):
            newDP0 = max(dp0, dp1 + prices[i])
            newDP1 = max(dp1, dp0 - prices[i])
            dp0, dp1 = newDP0, newDP1
        return dp0
        
"""
https://leetcode-cn.com/submissions/detail/131703814/

200 / 200 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 14.6 MB

执行用时：52 ms, 在所有 Python 提交中击败了53.25%的用户
内存消耗：14.6 MB, 在所有 Python 提交中击败了11.22%的用户
"""
