class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        res = []
        currMax = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= currMax:
                res.append(True)
            else:
                res.append(False)
        return res
        
"""
103 / 103 个通过测试用例
状态：通过
执行用时：24 ms
内存消耗：12.7 MB
"""
