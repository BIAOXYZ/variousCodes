class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        alphabeta = [chr(i) for i in range(ord('a'), ord('z')+1)]
        for i in range(len(alphabeta)-1, -1, -1):
            ch = alphabeta[i]
            if ch in s and ch.upper() in s:
                return ch.upper()
        return ''
    
"""
https://leetcode.cn/submissions/detail/326779270/

110 / 110 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 12.8 MB
"""
