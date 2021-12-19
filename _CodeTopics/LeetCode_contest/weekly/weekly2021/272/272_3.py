class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        i = 0
        currlen = 1
        res = 0
        while i < n-1:
            if prices[i] - prices[i+1] == 1:
                currlen += 1
                i += 1
                continue
            res += currlen * (currlen + 1) / 2
            currlen = 1
            i += 1
        res += currlen * (currlen + 1) / 2
        return res
    
"""
https://leetcode-cn.com/submissions/detail/249857930/

167 / 167 个通过测试用例
状态：通过
执行用时: 132 ms
内存消耗: 20.3 MB
"""
