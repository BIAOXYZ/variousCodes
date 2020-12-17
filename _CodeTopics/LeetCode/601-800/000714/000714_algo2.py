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
        
        # 同样的，类似 `000122_algo3.py`，这里也可以压缩状态，只需要两个变量就行。
        # 因为第i天的情况只跟前一天有关。
        dp0 = 0
        dp1 = -prices[0]

        for i in range(1, length):
            newDP0 = max(dp0, dp1 + prices[i] - fee)
            newDP1 = max(dp1, dp0 - prices[i])
            dp0, dp1 = newDP0, newDP1
        return dp0
        
"""
https://leetcode-cn.com/submissions/detail/131724453/

44 / 44 个通过测试用例
状态：通过
执行用时: 624 ms
内存消耗: 18.8 MB

执行用时：624 ms, 在所有 Python 提交中击败了86.49%的用户
内存消耗：18.8 MB, 在所有 Python 提交中击败了50.19%的用户
"""
