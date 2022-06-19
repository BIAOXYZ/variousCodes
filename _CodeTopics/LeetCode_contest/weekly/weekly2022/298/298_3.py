class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        n = len(s)
        if int(s, 2) <= k:
            return n
        
        for i in range(1, s.count('1')+1):
            tmp = s.replace('1', '0', i)
            if int(tmp, 2) <= k:
                return n - i
        return 0
    
"""
https://leetcode.cn/submissions/detail/326823920/

150 / 150 个通过测试用例
状态：通过
执行用时: 124 ms
内存消耗: 13 MB
"""
