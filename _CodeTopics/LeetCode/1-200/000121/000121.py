class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        length = len(prices)
        res = 0

        for i in range(length-1):
            tmp = max(prices[i+1:])
            res = max(res, tmp - prices[i])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/121357071/

200 / 200 个通过测试用例
状态：通过
执行用时: 4112 ms
内存消耗: 14.1 MB

执行用时：4112 ms, 在所有 Python 提交中击败了11.14%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了9.60%的用户
"""
