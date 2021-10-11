class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if dividend == 0:
            return 0
        elif (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        dividend, divisor = abs(dividend), abs(divisor)
        exponent = 0
        while dividend >= divisor*(2**exponent):
            exponent += 1
        
        res = 0
        while dividend >= divisor:
            if dividend >= divisor*(2**exponent):
                res += 2**exponent
                dividend -= divisor*(2**exponent)
            exponent -= 1
        return sign * res
        
"""
https://leetcode-cn.com/submissions/detail/227960845/

992 / 992 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.4 MB

执行用时：20 ms, 在所有 Python 提交中击败了90.09%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了5.53%的用户
"""
