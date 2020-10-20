class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """

        len1, len2 = len(name), len(typed)        
        ptr1 = ptr2 = 0

        while ptr1 <= len1 - 1 and ptr2 <= len2 - 1:
            if name[ptr1] == typed[ptr2]:
                ptr1 += 1; ptr2 += 1
            else:
                if ptr2 >= 1 and typed[ptr2] == typed[ptr2-1]:
                    ptr2 += 1
                    continue
                else:
                    return False
        
        def has_one_kind_of_letter(s, ch):
            for i in range(len(s)):
                if s[i] != ch:
                    return False
            return True

        if ptr1 != len1:
            return False
        else:
            if ptr2 == len2:
                return True
            elif has_one_kind_of_letter(typed[ptr2:], typed[ptr2-1]):
                return True
            else:
                return False
        
"""
https://leetcode-cn.com/submissions/detail/117360090/

84 / 84 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.9 MB

执行用时：16 ms, 在所有 Python 提交中击败了89.23%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了5.88%的用户
"""
