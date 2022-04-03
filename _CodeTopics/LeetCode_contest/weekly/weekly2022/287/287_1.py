class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        
        res = 0
        h1, h2 = current[:2], correct[:2]
        m1, m2 = current[3:], correct[3:]
        if m2 >= m1:
            res += int(h2) - int(h1)
            d = int(m2) - int(m1)
        elif m2 < m1:
            res += int(h2) - int(h1) - 1
            d = int(m2) - int(m1) + 60
        
        while d >= 15:
            res += 1
            d -= 15
        while d >= 5:
            res += 1
            d -= 5
        res += d
        return res
    
"""
https://leetcode-cn.com/submissions/detail/293975031/

255 / 255 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.1 MB
"""
