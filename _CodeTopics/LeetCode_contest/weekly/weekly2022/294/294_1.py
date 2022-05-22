class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        
        if letter not in s:
            return 0
        res = s.count(letter) * 1.0 / len(s)
        print res
        return int(res * 100)
    
"""
https://leetcode.cn/submissions/detail/316520366/

85 / 85 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.1 MB
"""
