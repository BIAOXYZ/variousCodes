class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        
        # 两重for循环优化了一下，但是感觉对于某些输入根本没用，
        # 比如：没有任何两个events可以合法的相交的情况。
        
        def are_legal_events(e1, e2):
            return e1[0] > e2[1] or e2[0] > e1[1]
        
        events.sort(key=lambda x:x[2], reverse=True)
        n = len(events)
        res = events[0][2]
        
        start, end = 0, n
        while start < end:
            breakFlag = False
            for i in range(start, end-1):
                for j in range(start+1, end):
                    if are_legal_events(events[i], events[j]):
                        res = max(res, events[i][2] + events[j][2])
                        breakFlag = True
                        end = j
                        break
                if breakFlag:
                    break
            start += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/233899673/

29 / 50 个通过测试用例
状态：超出时间限制
"""
"""
发现这个还没有第一个版本过的用例多。。。为啥优化没生效啊。。。
"""
