class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        def positive_divide(a, b):
            res = 0
            while a >= b:
                res += 1
                a -= b
            return res

        if dividend == 0:
            return 0
        elif (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return positive_divide(abs(dividend), abs(divisor))
        else:
            return -positive_divide(abs(dividend), abs(divisor))
        
"""
https://leetcode-cn.com/submissions/detail/227958589/

10 / 992 个通过测试用例
状态：超出时间限制

最后执行的输入：
-2147483648
-1
"""
