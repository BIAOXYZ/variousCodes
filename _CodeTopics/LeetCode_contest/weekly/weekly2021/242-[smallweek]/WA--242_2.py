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
        
        left, right = 1, 10000
        while left <= right:
            res = right
            mid = (left + right) / 2
            if speed_possible(mid):
                res = mid
                right = mid - 1
            else:
                left += mid + 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/180001991/

17 / 53 个通过测试用例
状态：解答错误

最后执行的输入：
[1,1,100000]
2.01
"""
