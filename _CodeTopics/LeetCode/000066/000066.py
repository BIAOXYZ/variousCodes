class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        length = len(digits)
        breakflag = False
        for i in range(length-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                breakflag = True
                break
        if breakflag:
            return digits
        else:
            pos = 0
            digits.insert(pos, 1)
            return digits
            
"""
https://leetcode-cn.com/submissions/detail/77876194/

109 / 109 个通过测试用例
状态：通过
执行用时：28 ms
内存消耗：12.6 MB
"""
