class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stk = []
        for tk in tokens:
            if not stk or tk not in ["+", "-", "*", "/"]:
                stk.append(int(tk))
            else:
                rightNum = stk.pop()
                leftNum = stk.pop()
                if tk == "+": stk.append(leftNum + rightNum)
                elif tk == "-": stk.append(leftNum - rightNum)
                elif tk == "*": stk.append(leftNum * rightNum)
                elif tk == "/": stk.append(int(leftNum * 1.0 / rightNum))
        return stk[0]
        
"""
https://leetcode-cn.com/submissions/detail/157372851/

20 / 20 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 14.3 MB

执行用时：28 ms, 在所有 Python 提交中击败了81.68%的用户
内存消耗：14.3 MB, 在所有 Python 提交中击败了76.96%的用户
"""
