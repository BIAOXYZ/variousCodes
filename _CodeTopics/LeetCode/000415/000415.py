class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        flag = 0
        len1, len2 = len(num1), len(num2)
        if len1 >= len2:
            longer, shorter, lenlonger, lenshorter = num1, num2, len1, len2
        else:
            longer, shorter, lenlonger, lenshorter = num2, num1, len2, len1
        
        res = ''
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
        
        # 最后如果还有进位需要处理下，比如 12+99，没有这句的话结果是11，本来应该是111。
        if flag == 1:
            res = '1' + res
        return res
        
"""
https://leetcode-cn.com/submissions/detail/94158175/

315 / 315 个通过测试用例
状态：通过
执行用时：52 ms
内存消耗：13.1 MB
"""
"""
执行用时：52 ms, 在所有 Python 提交中击败了28.99%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了33.33%的用户
"""
