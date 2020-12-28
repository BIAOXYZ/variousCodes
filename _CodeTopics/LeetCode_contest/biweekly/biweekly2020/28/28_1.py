class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        
        length = len(prices)
        if length == 1:
            return prices
        
        res = [None] * length
        for i in range(length):
            res[i] = prices[i]
            for j in range(i+1,length):
                if prices[j] <= prices[i]:
                    res[i] = prices[i] - prices[j]
                    break
        return res
    
"""
https://leetcode-cn.com/submissions/detail/78709545/

103 / 103 个通过测试用例
	状态：通过
执行用时：32 ms
内存消耗：12.9 MB
"""
