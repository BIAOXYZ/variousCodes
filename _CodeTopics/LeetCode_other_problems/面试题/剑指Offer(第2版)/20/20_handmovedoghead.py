import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = re.compile(r'^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$')
        return bool(pattern.match(s.strip()))
"""
https://leetcode-cn.com/submissions/detail/103869795/

1480 / 1480 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 12.7 MB
"""
"""
执行用时：40 ms, 在所有 Python 提交中击败了42.66%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了62.59%的用户
"""
