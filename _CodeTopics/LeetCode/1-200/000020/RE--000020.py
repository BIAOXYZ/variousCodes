class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for bracket in s:
            if bracket in ['(','[','{']:
                stack.append(bracket)
            else:
                # if条件语句过长换行的话用“\”，“\”和“or”之间空一格也行，紧挨着也可以。
                if (bracket == ')' and stack[-1] == '(') or \
                (bracket == ']' and stack[-1] == '[') or \
                (bracket == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
        return True if not stack else False
        
"""
https://leetcode-cn.com/submissions/detail/97851581/

7 / 76 个通过测试用例
状态：执行出错

执行出错信息：
Line 15: IndexError: list index out of range
最后执行的输入：
"]"
"""
