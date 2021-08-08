class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        
        w = ''
        i = 0
        while len(w) < len(s) and i < len(words):
            w += words[i]
            i += 1
        if w == s:
            return True
        return False
    
"""
https://leetcode-cn.com/submissions/detail/204485377/

346 / 346 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB
"""
