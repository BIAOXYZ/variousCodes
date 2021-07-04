class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        n = len(dist)
        dangerousDegree = [float(dist[i])/speed[i] for i in range(n)]
        dangerousDegree.sort()
        
        for minute in range(1, n):
            if dangerousDegree[minute] <= minute:
                return minute
        return n
    
"""
https://leetcode-cn.com/submissions/detail/192108393/

130 / 130 个通过测试用例
状态：通过
执行用时: 176 ms
内存消耗: 24.3 MB
"""
