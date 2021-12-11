class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ''
        for ch in s:
            if ord('A') <= ord(ch) <= ord('Z'):
                ch = chr(ord(ch) - ord('A') + ord('a'))
            res += ch
        return res
        
"""
https://leetcode-cn.com/submissions/detail/247605935/

执行用时：12 ms, 在所有 Python 提交中击败了85.44%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了23.30%的用户
通过测试用例：
114 / 114
"""
