class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        total = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
            else:
                continue
        return total
        
"""
执行结果：通过 显示详情
执行用时 : 48 ms, 在所有 Python 提交中击败了47.59%的用户
内存消耗 :13.7 MB, 在所有 Python 提交中击败了10.00%的用户
"""
"""
200 / 200 个通过测试用例
状态：通过
执行用时：48 ms
内存消耗：13.7 MB
"""
