import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        ctr = collections.Counter(s)
        res = 0
        flag = False
        for v in ctr.values():
            if v % 2 == 0:
                res += v
            else:
                flag = True
                res += v-1
        return res if not flag else res + 1
        
"""
https://leetcode-cn.com/submissions/detail/160655827/

95 / 95 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 12.9 MB

执行用时：36 ms, 在所有 Python 提交中击败了10.29%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了73.16%的用户
"""
