class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        
        n = len(stockPrices)
        if n == 1:
            return 0
        elif n == 2:
            return 1
        stockPrices.sort()
        
        def in_one_line(coor1, coor2, coor3):
            x1, y1 = coor1
            x2, y2 = coor2
            x3, y3 = coor3
            return (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1)
        
        res = 1
        for i in range(2, n):
            if not in_one_line(stockPrices[i-2], stockPrices[i-1], stockPrices[i]):
                res += 1
        return res
    
"""
https://leetcode.cn/submissions/detail/316542815/

79 / 79 个通过测试用例
状态：通过
执行用时: 372 ms
内存消耗: 42.9 MB
"""
