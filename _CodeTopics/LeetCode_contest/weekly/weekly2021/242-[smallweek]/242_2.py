class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        
        n = len(dist)
        if hour <= n - 1:
            return -1
        
        def speed_possible(s):
            time = 0
            for i in range(len(dist)-1):
                dis = dist[i]
                if dis % s == 0:
                    time += dis/s
                else:
                    time += dis/s + 1
            time += dist[-1] * 1.0 / s
            return time <= hour
        
        if type(hour) == type(1):
            maxNeedSpeed = 100000
        else:
            lastSpeed = int(dist[-1] / (hour - n + 1)) + 1
            maxNeedSpeed = max(100000, lastSpeed)
        left, right = 1, maxNeedSpeed
        res = right
        while left <= right:
            mid = (left + right) / 2
            if speed_possible(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/180011436/

53 / 53 个通过测试用例
状态：通过
执行用时: 1924 ms
内存消耗: 20.6 MB
"""
