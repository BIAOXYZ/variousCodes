class Solution(object):
    def numberOfRounds(self, startTime, finishTime):
        """
        :type startTime: str
        :type finishTime: str
        :rtype: int
        """
        
        s = [int(startTime[:2]), int(startTime[3:])]
        f = [int(finishTime[:2]), int(finishTime[3:])]
        print s, f
        if s[0] > f[0] or (s[0] == f[0] and s[1] > f[1]):
            f[0] += 24
        
        res = 0
        if f[1] < s[1]:
            f[1] += 60
            f[0] -= 1
        res += (f[0] - s[0]) * 4
        
        """
        startContain, endContain = 0, 0
        if s[1] == 0: startContain == 1
        elif 0 < s[1] <= 15: startContain == 2
        elif 15 < s[1] <= 30: startContain == 3
        elif 30 < s[1] <= 45: startContain == 4
        else: startContain == False

        if f[1] == 0: endContain == 1
        elif 0 < s[1] <= 15: endContain == 2
        elif 15 < s[1] <= 30: endContain == 3
        elif 30 < s[1] <= 45: endContain == 4
        else: startContain == 5
        """
        
        diff = (f[1] - s[1]) / 15
        if diff == 0:
            if s[1] not in [0, 15, 30, 45] and f[1] not in [0, 15, 30, 45]:
                diff -= 1            
        elif diff == 1:
            if s[1] not in [0, 15, 30, 45] and f[1] not in [0, 15, 30, 45]:
                diff -= 1
        elif diff == 2:
            if s[1] not in [0, 15, 30, 45] and f[1] not in [0, 15, 30, 45]:
                diff -= 1
        elif diff == 3:
            if s[1] not in [0, 15, 30, 45] and f[1] not in [0, 15, 30, 45, 60, 75, 90, 105, 120]:
                diff -= 1
        res += diff  
        return res
    
"""
https://leetcode-cn.com/submissions/detail/188152219/

41 / 73 个通过测试用例
状态：解答错误

最后执行的输入：
"04:54"
"18:51"
"""
