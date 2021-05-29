class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        if n < 3:
            return 0
        
        res = 0
        for i in range(n-2):
            if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i+2] != s[i]:
                res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/182010513/

160 / 160 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.3 MB
"""
