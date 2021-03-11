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
        
        stk = collections.deque(stk)
        res = stk.popleft()
        while stk:
            operator = stk.popleft()
            rightNum = stk.popleft()
            if operator == '+':
                res += rightNum 
            elif operator == '-':
                res -= rightNum
        return res
        
"""
https://leetcode-cn.com/submissions/detail/154004431/

109 / 109 个通过测试用例
状态：通过
执行用时: 132 ms
内存消耗: 16.6 MB

执行用时：132 ms, 在所有 Python 提交中击败了35.04%的用户
内存消耗：16.6 MB, 在所有 Python 提交中击败了60.59%的用户
"""
