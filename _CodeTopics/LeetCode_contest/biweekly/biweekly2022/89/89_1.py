class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        
        res1 = res2 = 1
        hour, minute= time[:2], time[3:]
        
        if hour == "??":
            res1 = 24
        elif hour[0] == "?":
            res1 = 3 if int(hour[1]) < 4 else 2
        elif hour[1] == "?":
            res1 = 10 if hour[0] in "01" else 4
        
        if minute == "??":
            res2 = 60
        elif minute[0] == "?":
            res2 = 6
        elif minute[1] == "?":
            res2 = 10
        
        return res1*res2
    
"""
https://leetcode.cn/submissions/detail/373337962/

53 / 53 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.2 MB
"""
