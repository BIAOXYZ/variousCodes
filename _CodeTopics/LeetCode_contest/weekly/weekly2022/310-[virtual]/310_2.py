class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        se = set()
        for ch in s:
            if ch not in se:
                se.add(ch)
            else:
                res += 1
                se = set([ch])
        return res + 1
    
"""
https://leetcode.cn/submissions/detail/361798774/

59 / 59 个通过测试用例
状态：通过
执行用时: 112 ms
内存消耗: 13.6 MB
"""
