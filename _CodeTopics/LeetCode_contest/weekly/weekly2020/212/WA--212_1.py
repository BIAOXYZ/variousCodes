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
        for i in range(1, length):
            timeList[i] = timeList[i] - timeList[i-1]
            if timeList[i] >= maxTime:
                maxTime = timeList[i]
                res = keysPressed[i]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/118403107/

27 / 101 个通过测试用例
状态：解答错误

输入：
[23,34,43,59,62,80,83,92,97]
"qgkzzihfc"
输出：
"f"
预期：
"q"
"""
