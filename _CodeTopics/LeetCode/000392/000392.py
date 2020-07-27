class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        lens, lent = len(s), len(t)
        pointer_s = pointer_t = 0

        while pointer_s < lens and pointer_t < lent:
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
                pointer_t += 1
            else:
                pointer_t += 1
        
        if pointer_s == lens:
            return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/91884307/

15 / 15 个通过测试用例
状态：通过
执行用时：28 ms
内存消耗：12.8 MB
"""
"""
执行用时：28 ms, 在所有 Python 提交中击败了39.09%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了100.00%的用户
"""
