from collections import deque
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = []
        stk = deque()
        for ch in s:
            if ch != ')':
                res.append(ch)
            else:
                while res[-1] != '(':
                    stk.append(res.pop())
                res.pop()
                while stk:
                    res.append(stk.popleft())
        return ''.join(res)
        
"""
https://leetcode-cn.com/submissions/detail/180871566/

38 / 38 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.1 MB

执行用时：28 ms, 在所有 Python 提交中击败了27.18%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了29.13%的用户
"""
