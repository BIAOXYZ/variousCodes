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
            # 这里也要考虑负数的情形，淦！
            return tmpList[0] if not isNeg else '-' + tmpList[0]
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
https://leetcode-cn.com/submissions/detail/225536450/

39 / 39 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.4 MB

执行用时：20 ms, 在所有 Python 提交中击败了33.33%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了6.48%的用户
"""
