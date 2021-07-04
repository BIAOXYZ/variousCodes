class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        n = len(dist)
        dangerousDegree = [float(dist[i])/speed[i] for i in range(n)]
        dangerousDegree.sort(reverse=True)
        
        for minute in range(n):
            dangerousDegree.pop()
            for i in range(n-1-minute):
                dangerousDegree[i] -= 1
                if dangerousDegree[i] <= 0:
                    return minute + 1
        return n
    
"""
https://leetcode-cn.com/submissions/detail/192103845/

120 / 130 个通过测试用例
状态：超出时间限制
"""
