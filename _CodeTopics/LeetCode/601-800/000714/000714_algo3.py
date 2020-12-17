class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        # 贪心算法实现：和 `000122_algo1.py` 类似，但是更复杂。主要是因为有手续费存在，
        # 所以不能简单地采用“只要第 i+1 天比第 i 天价格高，就可以把差价算利润”的策略了。
        #
        # 这里采用的策略是这样的：
        # - 假定第一天就买了，当前最低价就是第一天价格加上手续费。如果（在没卖出之前）发现某一天的（含fee）
        #   价格比当前最低价还低，那么把当前最低价更新成这个价格 + fee。 --> 也就是代码里elif分支。
        # - 一旦发现某个价格比（含手续费的）当前最低价还高，也就是能盈利了，就把盈利部分加上；
        #   但是这样不意味着结束，因为可能后一天（第i+1天）价格更高一点，但是此时再加新的利润时不能
        #   再用原来那个当前最低价了，而应该是用第i天的价格。 --> 也就是代码里if分支。
        """
        这个图能大概说明下策略：
        。              。
           。         。
              。    。
                 。
        """

        length = len(prices)
        if length < 2:
            return 0
        
        total = 0
        currMinPrice = prices[0] + fee
        for i in range(1, length):
            if prices[i] > currMinPrice:
                total += prices[i] - currMinPrice
                # 这句最关键！因为前面肯定减过一次带手续费fee的currMinPricele了，
                # 所以这个分支里更新的currMinPrice是不用再加上fee的。
                currMinPrice = prices[i]
            elif prices[i] + fee < currMinPrice:
                currMinPrice = prices[i] + fee
        return total
        
"""
https://leetcode-cn.com/submissions/detail/131745981/

44 / 44 个通过测试用例
状态：通过
执行用时: 544 ms
内存消耗: 18.9 MB

执行用时：544 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：18.9 MB, 在所有 Python 提交中击败了47.45%的用户
"""
