class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        length = len(points)
        points.sort()
        res = 0
        
        for i in range(1,length):
            res = max(res, points[i][0] - points[i-1][0])
        return res
    
"""
https://leetcode-cn.com/submissions/detail/120038360/

52 / 52 个通过测试用例
状态：通过
执行用时: 324 ms
内存消耗: 39.1 MB
"""
