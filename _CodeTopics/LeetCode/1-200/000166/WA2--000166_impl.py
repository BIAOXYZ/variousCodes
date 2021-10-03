class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

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
        return res if not repetend else res + repetend
        
"""
https://leetcode-cn.com/submissions/detail/225536194/

37 / 39 个通过测试用例
状态：解答错误

输入：
-50
8
输出：
"-7.75"
预期结果：
"-6.25"
"""
