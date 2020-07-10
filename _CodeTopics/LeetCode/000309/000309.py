class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        length = len(prices)
        if length <= 1:
            return 0

        dp = [[0 for i in range(3)] for j in range(length)]
        dp[0][0] = 0
        dp[0][1] = 0
        dp[0][2] = -prices[0]
        ## print dp

        # dp[i][0] 第i天（结束）时，股票已经卖出去且不在冷冻期。
        # dp[i][1] 第i天（结束）时，股票已经卖出去且在冷冻期（也就是恰好在第i-1天卖出去）。
        # dp[i][2] 第i天（结束）时，手里还持有股票。
        for i in range(1,length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            # 这个推起来其实更直观（第i天处于冷冻状态，那肯定是前一天还有股票），
            # 但是还是先写的下面那行。。。
            dp[i][1] = dp[i-1][2] + prices[i]
            # 这个推起来最直观，其实写的时候是先写的这行。。。
            dp[i][2] = max(dp[i-1][2], dp[i-1][0]-prices[i])
        return max(dp[length-1][0], dp[length-1][1])
        
"""
https://leetcode-cn.com/submissions/detail/86624027/

211 / 211 个通过测试用例
状态：通过
执行用时：24 ms
内存消耗：13.3 MB
"""
"""
执行用时：24 ms, 在所有 Python 提交中击败了91.10%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了100.00%的用户
"""
