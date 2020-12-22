import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
      
        dic = {}
        for i, ch in enumerate(s):
            if dic.has_key(ch):
                dic[ch] = -1
            else:
                dic[ch] = i
        
        vals = dic.values()
        while -1 in vals:
            vals.remove(-1)
        return -1 if not vals else min(vals)
        
"""
https://leetcode-cn.com/submissions/detail/133019982/

104 / 104 个通过测试用例
状态：通过
执行用时: 88 ms
内存消耗: 13.3 MB

执行用时：88 ms, 在所有 Python 提交中击败了93.02%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了71.99%的用户
"""
