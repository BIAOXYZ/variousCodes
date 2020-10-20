class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """

        # 用了和官方答案类似的实现。尽管原理都是双指针，但是官方这个实现确实有亮点：
        # 在while循环里只考虑 ptr2 的位置，这样对于形如
        # "a"
        # "aaaa"
        # 的输入，也不用考虑while循环出来后还得再处理 typed 这个串可能的剩下的字符的问题。 
        ptr1 = ptr2 = 0
        while ptr2 < len(typed):
            if ptr1 < len(name) and name[ptr1] == typed[ptr2]:
                ptr1 += 1
                ptr2 += 1
            elif ptr2 > 0 and typed[ptr2] == typed[ptr2-1]:
                ptr2 += 1
            else:
                return False
        return ptr1 == len(name)
        
"""
https://leetcode-cn.com/submissions/detail/117360759/

84 / 84 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.8 MB

执行用时：16 ms, 在所有 Python 提交中击败了89.23%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了5.88%的用户
"""
