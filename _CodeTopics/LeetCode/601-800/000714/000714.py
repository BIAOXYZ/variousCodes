class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        length = len(prices)
        if length < 2:
            return 0
        
        # 这个和 `LC122 买卖股票的最佳时机 II` 的动态规划本质上没有任何区别。
        # 具体代码中唯一的一点区别就是：卖出股票的时候需要多减去一个手续费值。
        # 对比这个代码和 `000122_algo2.py` 就知道了。
        dp = [[0 for i in range(2)] for j in range(length)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[length-1][0]
        
"""
https://leetcode-cn.com/submissions/detail/131721570/

44 / 44 个通过测试用例
状态：通过
执行用时: 896 ms
内存消耗: 24.5 MB

执行用时：896 ms, 在所有 Python 提交中击败了19.69%的用户
内存消耗：24.5 MB, 在所有 Python 提交中击败了5.09%的用户
"""
