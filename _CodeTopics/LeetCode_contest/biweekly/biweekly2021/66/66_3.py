class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        
        x1, y1 = startPos[0], startPos[1]
        x2, y2 = homePos[0], homePos[1]
        rowcost, colcost = 0, 0
        if x1 != x2:
            small, large = min(x1, x2), max(x1, x2)
            for ind in range(small+1, large):
                rowcost += rowCosts[ind]
            rowcost += rowCosts[x2]
        if y1 != y2:
            small, large = min(y1, y2), max(y1, y2)
            for ind in range(small+1, large):
                colcost += colCosts[ind]
            colcost += colCosts[y2]
        return rowcost + colcost
    
"""
https://leetcode-cn.com/submissions/detail/242940957/

69 / 69 个通过测试用例
状态：通过
执行用时: 84 ms
内存消耗: 23.2 MB
"""
