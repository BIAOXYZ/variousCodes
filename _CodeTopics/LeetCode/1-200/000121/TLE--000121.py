class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        length = len(prices)
        res = 0

        for i in range(length-1):
            for j in range(i+1, length):
                res = max(res, prices[j] - prices[i])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/121355998/

199 / 200 个通过测试用例
状态：超出时间限制

用例太长，省略。
"""
