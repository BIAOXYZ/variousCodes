class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """

        # 其实这题就是考察栈，而且第一时间也写了栈的实现。
        # 但就是想试试不用栈的方法，估计会超时。

        S = list(S)
        flagHasAdjacentLetter = True

        while flagHasAdjacentLetter:
            # 先手动变成False，后面for循环里如果有连续两个相同的再变成True。主要是为了while循环，因为如果
            # 一开始赋成False，while循环就开始不了了。。。
            flagHasAdjacentLetter = False
            stk = [S[0]]
            for i in range(1, len(S)):
                if not stk or S[i] != S[i-1]:
                    stk.append(S[i])
                else:
                    flagHasAdjacentLetter = True
                    stk.pop()
            if not stk:
                return ""
            else:
                S = stk
        return "".join(stk)
        
"""
https://leetcode-cn.com/submissions/detail/152751933/

35 / 98 个通过测试用例
状态：解答错误

输入：
"abbbabaaa"
输出：
"a"
预期：
"ababa"
"""
