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
        
        dic = {}
        i = 0
        repetend = ''
        while remainder != 0:
            remainder *= 10
            quotient = remainder / denominator
            remainder %= denominator
            if remainder == 0:
                tmpList.append(str(quotient))
                break 
            if not dic.has_key(remainder):
                dic[remainder] = i
                tmpList.append(str(quotient))
                i += 1
            else:
                repetend = '('
                for ind in range(dic[remainder], i):
                    # 这里是因为 tmpList 前两个位置分别是除法的整数部分和小数点。
                    repetend += tmpList[ind+2]
                repetend += ')'
                for ind in range(i - dic[remainder]):
                    tmpList.pop()
                break
        
        res = ''.join(tmpList)
        return res if not repetend else res + repetend
        
"""
https://leetcode-cn.com/submissions/detail/225531797/

31 / 39 个通过测试用例
状态：解答错误

输入：
1
6
输出：
"0.(1)"
预期结果：
"0.1(6)"
"""
