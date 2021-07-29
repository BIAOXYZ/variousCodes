class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

        res = 0
        for ch in columnTitle:
            res *= 26
            res += ord(ch) - ord('A') + 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/201219733/

1002 / 1002 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.7 MB

执行用时：20 ms, 在所有 Python 提交中击败了80.74%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了98.99%的用户
"""
