class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        
        # 看起来是可以用一些匹配的手段加速，但是还是先暴力了！
        
        lenp = len(part)
        while s.find(part) != -1:
            i = s.find(part)
            s = s[:i] + s[i+lenp:]
        return s
    
"""
https://leetcode-cn.com/submissions/detail/189981928/

77 / 77 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.2 MB
"""
