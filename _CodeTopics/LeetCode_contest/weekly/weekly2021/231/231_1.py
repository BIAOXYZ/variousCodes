class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        flagZero = False
        for i in range(1, len(s)):
            if not flagZero and s[i] == '0':
                flagZero = True
            if flagZero and s[i] == '1':
                return False
        return True
    
"""
https://leetcode-cn.com/submissions/detail/151989679/

191 / 191 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 12.9 MB
"""
