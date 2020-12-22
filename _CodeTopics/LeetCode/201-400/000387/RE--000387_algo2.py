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
        length = len(vals)
        if length > 1:
            while -1 in vals:
                vals.remove(-1)
            return min(vals)
        elif length == 1:
            return vals[0]
        else:
            return -1
        
"""
https://leetcode-cn.com/submissions/detail/133019901/

6 / 104 个通过测试用例
状态：执行出错

执行出错信息：
Line 21: ValueError: min() arg is an empty sequence
最后执行的输入：
"aadadaad"
"""
