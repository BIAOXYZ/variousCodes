class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        ctr = collections.Counter(s)
        tmp = set(ctr.values())
        return True if len(tmp) == 1 else False
    
"""
https://leetcode-cn.com/submissions/detail/199414816/

132 / 132 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.9 MB
"""
