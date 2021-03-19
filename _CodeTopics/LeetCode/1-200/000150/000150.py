class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stk = []
        for tk in tokens:
            if not stk or tk not in ["+", "-", "*", "/"]:
                stk.append(tk)
            else:
                rightNum = stk.pop()
                leftNum = stk.pop()
                ##print leftNum + tk + rightNum
                if tk == "/" and int(leftNum) * int(rightNum) < 0  and abs(int(leftNum)) % abs(int(rightNum)) != 0:
                    stk.append(str(eval(leftNum + tk + rightNum) + 1))
                else:
                    stk.append(str(eval(leftNum + tk + rightNum)))
        return int(stk[0])
        
"""
https://leetcode-cn.com/submissions/detail/157365997/

20 / 20 个通过测试用例
状态：通过
执行用时: 68 ms
内存消耗: 14.3 MB

执行用时：68 ms, 在所有 Python 提交中击败了7.85%的用户
内存消耗：14.3 MB, 在所有 Python 提交中击败了69.11%的用户
"""
