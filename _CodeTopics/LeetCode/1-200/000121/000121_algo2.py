class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        length = len(prices)
        if length < 2:
            return 0
        
        maxProfit = 0
        currMinPrice = prices[0]
        for i in range(1, length):
            maxProfit = max(maxProfit, prices[i] - currMinPrice)
            currMinPrice = min(currMinPrice, prices[i])
        return maxProfit
        
"""
https://leetcode-cn.com/submissions/detail/121782733/

200 / 200 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 14 MB

执行用时：32 ms, 在所有 Python 提交中击败了40.60%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了12.19%的用户
"""
