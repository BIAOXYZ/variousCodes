class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def binaryToDecimal(binarystr):
            decimal = 0
            length = len(binarystr)
            for i in range(length):
                if binarystr[i] is '1':
                    decimal += 2 ** ((length-1) - i)
            return decimal
        
        decimalnum = binaryToDecimal(s)
        step = 0
        
        while decimalnum != 1:
            if decimalnum % 2 == 1:
                decimalnum += 1
                step += 1
            else:
                decimalnum = decimalnum // 2
                step += 1
        return step
    
"""
提交结果：超出时间限制
0 / 73 个通过测试用例
最后执行的输入： "1101" 
"""
