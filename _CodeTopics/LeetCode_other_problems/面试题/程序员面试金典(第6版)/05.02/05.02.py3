class Solution:
    def printBin(self, num: float) -> str:

        res = ['0.']
        leftDigitNum = 31
        i = 1
        while num > 0 and i < leftDigitNum:
            curr = 2**(-i)
            if num >= curr:
                res.append('1')
                num -= curr
            else:
                res.append('0')
            i += 1
        if num > 0:
            return "ERROR"
        else:
            return ''.join(res)
        
"""
https://leetcode.cn/submissions/detail/408317434/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
87.07%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
27.59%
的用户
通过测试用例：
33 / 33
"""
