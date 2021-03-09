class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 服了，这TM怎么就超时了。。。我怀疑又是python效率的问题！

        length = len(s)
        stk = []
        for i, ch in enumerate(s):
            if ch.isnumeric():
                if not stk or stk[-1] == '(':
                    stk.append(int(ch))
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
            ##print stk
        return stk[0]
        
"""
https://leetcode-cn.com/submissions/detail/153205524/

8 / 39 个通过测试用例
状态：解答错误

输入：
"2147483647"
输出：
2
预期：
2147483647
"""
"""
妈蛋，甚至连超时的用例都没跑到，艹。。。
"""
