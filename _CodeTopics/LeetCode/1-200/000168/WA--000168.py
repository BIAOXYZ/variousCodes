class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        res = ""
        while columnNumber > 26:
            remainder = columnNumber % 26
            res = chr(remainder + (ord("A") - 1)) + res
            columnNumber /= 26
        res = chr(columnNumber + (ord("A") - 1)) + res
        return res
        
"""
https://leetcode-cn.com/submissions/detail/190579357/

16 / 18 个通过测试用例
状态：解答错误

最后执行的输入：
52
输出：
"B@"
预期结果：
"AZ"
"""
