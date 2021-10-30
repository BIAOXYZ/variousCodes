class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        
        # 感觉这个有超时的危险，因为下面的两重for循环还是可以优化的。
        
        def are_legal_events(e1, e2):
            return e1[0] > e2[1] or e2[0] > e1[1]
        
        events.sort(key=lambda x:x[2], reverse=True)
        n = len(events)
        res = events[0][2]
        for i in range(n-1):
            for j in range(i+1, n):
                if are_legal_events(events[i], events[j]):
                    res = max(res, events[i][2] + events[j][2])
                    break
        return res
    
"""
https://leetcode-cn.com/submissions/detail/233889716/

40 / 50 个通过测试用例
状态：超出时间限制
"""
