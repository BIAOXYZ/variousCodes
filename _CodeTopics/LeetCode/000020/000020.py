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
                if (bracket == ')' and stack != [] and stack[-1] == '(') or \
                (bracket == ']' and stack != [] and stack[-1] == '[') or \
                (bracket == '}' and stack != [] and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
        return True if not stack else False
        
"""
https://leetcode-cn.com/submissions/detail/97855880/

76 / 76 个通过测试用例
状态：通过
执行用时：24 ms
内存消耗：12.7 MB
"""
"""
执行用时：24 ms, 在所有 Python 提交中击败了62.58%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了82.23%的用户
"""
