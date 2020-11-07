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
            # 动态规划法实现中发现同样的现象：下面两行代码换位置也没问题！
            # 后来想想明白了：其实正确的做法就是应该是“后计算新的currMinPrice”，因为第i天
            # 本身的价格即使比前面的都小也不应该考虑在内（毕竟假定的是第i天卖出时的获利）。
            #
            # 但是为什么先算进去也不会错呢？因为要么就是前面某天的价格是currMinPrice，此时无影响；要么
            # 就算第i天的价格是currMinPrice，此时算出来的maxProfit是0（而本来应是负数），不论0还是负数，
            # 再和之前的最高价一起求max值，都没啥区别。
            dp[i] = max(dp[i-1], prices[i] - currMinPrice)
            currMinPrice = min(currMinPrice, prices[i])
        return dp[length-1]
        
"""
https://leetcode-cn.com/submissions/detail/121783551/

200 / 200 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 14.3 MB

执行用时：28 ms, 在所有 Python 提交中击败了58.66%的用户
内存消耗：14.3 MB, 在所有 Python 提交中击败了7.54%的用户
"""
