class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        
        times = [0] * n
        m = len(logs)
        userId, time = logs[0]
        times[userId] = time
        
        for i in range(1, m):
            userId, time = logs[i][0], logs[i][1] - logs[i-1][1]
            times[userId] = max(times[userId], time)
        return times.index(max(times))
    
"""
https://leetcode.cn/submissions/detail/371144106/

514 / 514 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 13 MB
"""
