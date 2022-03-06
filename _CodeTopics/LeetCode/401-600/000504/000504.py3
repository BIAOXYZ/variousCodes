class Solution:
    def convertToBase7(self, num: int) -> str:

        res = []
        if num == 0:
            return '0'
        elif num > 0:
            negativeFlag = '' 
        elif num < 0:
            num = -num
            negativeFlag = '-'
        
        while num > 0:
            quotient, remainder = num // 7, num % 7
            res.append(str(remainder))
            num = quotient
        res.reverse()
        return negativeFlag + ''.join(res)
        
"""
https://leetcode-cn.com/submissions/detail/278553933/

执行用时：36 ms, 在所有 Python3 提交中击败了52.62%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了91.76%的用户
通过测试用例：
241 / 241
"""
