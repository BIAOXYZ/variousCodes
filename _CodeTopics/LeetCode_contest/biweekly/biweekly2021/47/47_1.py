class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        
        n = len(points)
        res = -1
        currDistance = float('inf')
        for i in range(n):
            if points[i][0] == x or points[i][1] == y:
                newDistance = abs(points[i][0] - x) + abs(points[i][1] - y)
                if newDistance < currDistance:
                    res = i
                    currDistance = newDistance
        return res
    
"""
https://leetcode-cn.com/submissions/detail/151894984/

101 / 101 个通过测试用例
状态：通过
执行用时: 96 ms
内存消耗: 16.6 MB
"""
