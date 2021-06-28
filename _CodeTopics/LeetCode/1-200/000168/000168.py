class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        res = ""
        while columnNumber > 26:
            remainder = columnNumber % 26
            if remainder == 0:
                remainder = 26
                columnNumber -= 26
            res = chr(remainder + (ord("A") - 1)) + res
            columnNumber /= 26
        res = chr(columnNumber + (ord("A") - 1)) + res
        return res
        
"""
https://leetcode-cn.com/submissions/detail/190580190/

18 / 18 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.2 MB

执行用时：16 ms, 在所有 Python 提交中击败了78.15%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.46%的用户
"""
