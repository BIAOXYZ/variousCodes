class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        isNeg = False
        if numerator * denominator < 0:
            isNeg = True
            numerator = abs(numerator)
            denominator = abs(denominator)

        integerPart = numerator / denominator
        tmpList = [str(integerPart)]
        remainder = numerator % denominator
        if remainder == 0:
            return tmpList[0]
        else:
            tmpList.append('.')
        
        dic = {remainder:0}
        i = 1
        repetend = ''
        while remainder != 0:
            remainder *= 10
            quotient = remainder / denominator
            remainder %= denominator
            tmpList.append(str(quotient))
            if remainder == 0:    
                break 
            if not dic.has_key(remainder):
                dic[remainder] = i
                i += 1
            else:
                repetend += ')'
                for ind in range(i - dic[remainder]):
                    repetend = tmpList.pop() + repetend
                repetend = '(' + repetend
                break
        
        res = ''.join(tmpList)
        if isNeg:
            res = '-' + res
        return res if not repetend else res + repetend
        
"""
https://leetcode-cn.com/submissions/detail/225536329/

38 / 39 个通过测试用例
状态：解答错误

输入：
-2147483648
1
输出：
"2147483648"
预期结果：
"-2147483648"
"""
"""
淦！
"""
