class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # 动态规划实现。其中 dp[i] 表示第i天卖出时能获得的最大利润。

        length = len(prices)
        if length < 2:
            return 0
        
        dp = [0 for i in range(length)]
        currMinPrice = prices[0]

        for i in range(1, length):
            currMinPrice = min(currMinPrice, prices[i])
            dp[i] = max(dp[i-1], prices[i] - currMinPrice)
        return dp[length-1]
        
"""
https://leetcode-cn.com/submissions/detail/121783270/

200 / 200 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 14.5 MB

执行用时：24 ms, 在所有 Python 提交中击败了77.28%的用户
内存消耗：14.5 MB, 在所有 Python 提交中击败了6.43%的用户
"""
