class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """

        signs = ["*", "/", "+", "-"]
        signInd = 0
        tmpRes = N
        tmpStk = []

        while N > 1:
            currSign = signs[signInd % 4]
            currNum = N - 1 
            if currSign == "*":
                tmpRes *= currNum
            elif currSign == "/":
                if not tmpStk:
                    tmpRes /= currNum
                else:
                    tmpRes = tmpStk.pop() - tmpRes / currNum
            elif currSign == "+":
                tmpRes += currNum
            elif currSign == "-":
                tmpStk.append(tmpRes)
                tmpRes = currNum
            N -= 1
            signInd += 1
        if not tmpStk:
            return tmpRes
        else:
            return tmpStk[-1] - tmpRes
        
"""
https://leetcode-cn.com/submissions/detail/162389854/

84 / 84 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 13 MB

执行用时：56 ms, 在所有 Python 提交中击败了34.78%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了69.57%的用户
"""
