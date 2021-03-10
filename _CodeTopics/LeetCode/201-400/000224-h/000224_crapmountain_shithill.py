class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        stk = []
        for i, ch in enumerate(s):
            if ch.isdigit():
                if not stk or stk[-1] == '(':
                    stk.append(int(ch))
                # 这里修复多位数字的情况。
                elif type(stk[-1]) == type(1):
                    stk.append(10 * stk.pop() + int(ch))
                    # 这里连续数字处理完了，额外计算一次。要分末尾和非末尾两种情况。
                    if ((i + 1 < len(s) and not s[i+1].isdigit()) or (i == len(s) - 1)) and len(stk) > 1 and stk[-2] in ['+', '-']:
                        rightNum = stk.pop()
                        sign = stk.pop()
                        leftNum = stk.pop()
                        if sign == '+':
                            stk.append(leftNum + rightNum)
                        elif sign == '-':
                            stk.append(leftNum - rightNum)
                elif stk[-1] == '+' or (stk[-1] == '-' and len(stk) > 1 and type(stk[-2]) == type(1)):
                    # 如果下一位还是数字，那暂时还不能算，得等数字读完了才行，比如"1-10-("，不能先算1-1。
                    if i + 1 < len(s) and s[i+1].isdigit():
                        stk.append(int(ch))
                    else:
                        sign = stk.pop()
                        leftNum = stk.pop()
                        if sign == '+':
                            stk.append(leftNum + int(ch))
                        elif sign == '-':
                            stk.append(leftNum - int(ch))
                # 此时的 '-' 是负号的意思。
                elif stk[-1] == '-' and (len(stk) == 1 or type(stk[-2]) != type(1)):
                    stk.pop()
                    stk.append(-int(ch))
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
                elif stk[-1] == '+' or (stk[-1] == '-' and len(stk) > 1 and type(stk[-2]) == type(1)):
                    sign = stk.pop()
                    leftNum = stk.pop()
                    if sign == '+':
                        stk.append(leftNum + rightNum)
                    elif sign == '-':
                        stk.append(leftNum - rightNum)
                # 此时的 '-' 是负号的意思。
                elif stk[-1] == '-' and (len(stk) == 1 or type(stk[-2]) != type(1)):
                    stk.pop()
                    stk.append(-rightNum)
            ##print "curr s is:", s[:i+1]
            ##print "this elem is: ", ch
            ##print stk, "\n"
        return stk[0]
        
"""
https://leetcode-cn.com/submissions/detail/153557005/

39 / 39 个通过测试用例
状态：通过
执行用时: 176 ms
内存消耗: 14 MB
提交时间：1 分钟前

执行用时：176 ms, 在所有 Python 提交中击败了27.50%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了90.00%的用户
"""
