class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        
        length = len(releaseTimes)
        timeList = releaseTimes[:]
        
        maxTime, res = timeList[0], keysPressed[0]
        for i in range(length-1,0,-1):
            timeList[i] = timeList[i] - timeList[i-1]
            if timeList[i] > maxTime:
                maxTime = timeList[i]
                res = keysPressed[i]
        print timeList
        return res
    
"""
https://leetcode-cn.com/submissions/detail/118405497/

101 / 101 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13.1 MB
"""
