class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 艹他大爷，没法单步真是生草，还是不知道那个很长的输入怎么不对的，只能是把"2147483647"这个错误用例修一下。
        # 明天换个笔记本单步调一下。

        length = len(s)
        stk = []
        for i, ch in enumerate(s):
            if ch.isnumeric():
                if not stk or stk[-1] == '(':
                    stk.append(int(ch))
                # 这里修复多位数字的情况
                elif type(stk[-1]) == type(1):
                    stk.append(10 * stk.pop() + int(ch))
                elif stk[-1] == '+' or stk[-1] == '-':
                    sign = stk.pop()
                    leftNum = stk.pop()
                    if sign == '+':
                        stk.append(leftNum + int(ch))
                    elif sign == '-':
                        stk.append(leftNum - int(ch))
            elif ch == '+' or ch == '-':
                stk.append(ch)
            elif ch == '(':
                stk.append(ch)
            elif ch == ')':
                rightNum = stk.pop()
                # 这个是把左括号pop出去。
                stk.pop()
                if not stk:
                    stk.append(rightNum)
                elif stk[-1] == '+' or stk[-1] == '-':
                    sign = stk.pop()
                    leftNum = stk.pop()
                    if sign == '+':
                        stk.append(leftNum + rightNum)
                    elif sign == '-':
                        stk.append(leftNum - rightNum)
            ##print stk, "\n"
        return stk[0]
        
"""
https://leetcode-cn.com/submissions/detail/153206572/

11 / 39 个通过测试用例
状态：执行出错

执行出错信息：
Line 22: IndexError: pop from empty list
最后执行的输入：
"-2+ 1"
"""
