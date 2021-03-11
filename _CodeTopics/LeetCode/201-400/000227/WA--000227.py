class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 这个题比 LC224 简单就简单在：1.没有括号；2.没有负数。尽管这题多了乘除法，但是相比 LC224 还是简单了很多。

        length = len(s)
        stk = []
        for i, ch in enumerate(s):
            if ch.isdigit():
                if not stk:
                    stk.append(int(ch))
                elif type(stk[-1]) == type(1):
                    stk.append(10 * stk.pop() + int(ch))
                    if ((i < length - 1 and not s[i+1].isdigit()) or i == length - 1) and len(stk) > 1 and stk[-2] in ['*', '/']:
                        rightNum = stk.pop()
                        operator = stk.pop()
                        leftNum = stk.pop()
                        if operator == '*':
                            stk.append(leftNum * rightNum)
                        elif operator == '/':
                            stk.append(leftNum / rightNum)
                elif stk[-1] in ['+', '-', '*', '/']:
                    stk.append(int(ch))
                    if ((i < length - 1 and not s[i+1].isdigit()) or i == length - 1) and len(stk) > 1 and stk[-2] in ['*', '/']:
                        rightNum = stk.pop()
                        operator = stk.pop()
                        leftNum = stk.pop()
                        if operator == '*':
                            stk.append(leftNum * rightNum)
                        elif operator == '/':
                            stk.append(leftNum / rightNum)
            elif ch in ['+', '-', '*', '/']:
                stk.append(ch)
            ##print "curr s is:", s[:i+1]
            ##print "this elem is: ", ch
            ##print stk, "\n"
        
        res = stk.pop()
        while stk:
            operator = stk.pop()
            leftNum = stk.pop()
            if operator == '+':
                res = leftNum + res
            elif operator == '-':
                res = leftNum - res
        return res
        
"""
https://leetcode-cn.com/submissions/detail/153999041/

86 / 109 个通过测试用例
状态：解答错误

输入：
"1-1+1"
输出：
-1
预期：
1
"""
