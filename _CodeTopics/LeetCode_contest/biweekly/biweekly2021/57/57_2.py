class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
         
        n = len(times)
        dic = {tuple(times[i]):i for i in range(n)}
        times.sort(key = lambda x : x[0])
        if dic[tuple(times[0])] == targetFriend:
            return 0
        
        seats = [-1 for _ in range(n)]
        # 第 0 个座位肯定被 0 个人占着，在他离开的时间才能释放。
        seats[0] = times[0][1]
        for i in range(1, n):
            arrival, leave = times[i][0], times[i][1]
            j = 0
            while arrival < seats[j] and seats[j] != -1:
                j += 1
            if dic[tuple(times[i])] != targetFriend:
                seats[j] = leave
            else:
                return j
            
"""
https://leetcode-cn.com/submissions/detail/199427630/

60 / 60 个通过测试用例
状态：通过
执行用时: 7008 ms
内存消耗: 18 MB
"""
