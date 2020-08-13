class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def string_multiply_with_single(s, ch):
            carryflag, res = 0, ''
            for i in range(len(s)-1,-1,-1):
                tmp = int(s[i]) * int(ch) + carryflag
                res = str(tmp % 10) + res
                carryflag = tmp / 10
            # 前面那个提交`deliberate-WA--000043.py`虽然发现了错误用例，但是实在也没时间去
            # 单步调。结果一个更简单的多的错误用例一下子就把问题明确了："9" * "9" = "1"。
            # 所以其实就是这里忘了考虑新增的进位了。。。
            if carryflag > 0:
                res = str(carryflag) + res
            return res
        
        # 这里几乎就是把`000415.py`的内容绝大部分复制过来了。。。
        def string_add(num1, num2):
            flag, res = 0, ''
            len1, len2 = len(num1), len(num2)
            if len1 >= len2:
                longer, shorter, lenlonger, lenshorter = num1, num2, len1, len2
            else:
                longer, shorter, lenlonger, lenshorter = num2, num1, len2, len1
            for i in range(-1,-lenshorter-1,-1):
                summation = int(longer[i]) + int(shorter[i]) + flag
                if summation >= 10:
                    res = str(summation % 10) + res
                    flag = 1
                else:
                    res = str(summation) + res
                    flag = 0
            for j in range(-lenshorter-1,-lenlonger-1,-1):
                summation = int(longer[j]) + flag
                if summation >= 10:
                    res = str(summation % 10) + res
                    flag = 1
                else:
                    res = str(summation) + res
                    flag = 0
            if flag == 1:
                res = '1' + res
            return res

        if num1 == '0' or num2 == '0':
            return '0'
        res = ''
        len1, len2 = len(num1), len(num2)
        if len1 >= len2:
            longer, shorter, lenlonger, lenshorter = num1, num2, len1, len2
        else:
            longer, shorter, lenlonger, lenshorter = num2, num1, len2, len1
        
        for i in range(lenshorter-1,-1,-1):
            tmpres = string_multiply_with_single(longer, shorter[i])
            # 乘完还要在末尾加一定数量的0
            for j in range(lenshorter-1-i):
                tmpres = tmpres + '0'
            res = string_add(res, tmpres)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/97683499/

311 / 311 个通过测试用例
状态：通过
执行用时：496 ms
内存消耗：12.6 MB
"""
"""
执行用时：496 ms, 在所有 Python 提交中击败了17.65%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了71.87%的用户
"""
