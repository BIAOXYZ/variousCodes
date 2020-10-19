class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        lena, lenb = len(a), len(b)
        maxlen, minlen = max(lena,lenb), min(lena,lenb)
        zeroPrefix = ''
        for i in range(maxlen - minlen):
            zeroPrefix = zeroPrefix + '0'
        if lena < maxlen:
            a = zeroPrefix + a
        if lenb < maxlen:
            b = zeroPrefix + b

        carryBit, res = '0', ''
        for i in range(-1,-maxlen-1,-1):
            tempstr = ''.join([a[i],b[i],carryBit])
            if tempstr.count('1') == 3:
                res = '1' + res
                carryBit = '1'
            elif tempstr.count('1') == 2:
                res = '0' + res
                carryBit = '1'
            elif tempstr.count('1') == 1:
                res = '1' + res
                carryBit = '0'
            else:
                res = '0' + res
                carryBit = '0'
        if carryBit == '1':
            res = '1' + res
        return res
        
"""
https://leetcode-cn.com/submissions/detail/81431424/

294 / 294 个通过测试用例
状态：通过
执行用时：28 ms
内存消耗：12.7 MB
"""
