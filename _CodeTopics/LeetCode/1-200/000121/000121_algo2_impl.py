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
            currMinPrice = min(currMinPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - currMinPrice)
        return maxProfit
        
"""
https://leetcode-cn.com/submissions/detail/121782979/

200 / 200 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13.9 MB

执行用时：32 ms, 在所有 Python 提交中击败了40.60%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了15.27%的用户
"""
"""
这个和 000121_algo2.py 相比只是第15行和第16行交换了下位置。因为一时没想出来“先算当前最低价，然后用当前股价去减”
和“先用当前股价去减，然后再算新的最低价”是否会影响正确性，所以先试试了。。。
"""
