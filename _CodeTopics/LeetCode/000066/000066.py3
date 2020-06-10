class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
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
https://leetcode-cn.com/submissions/detail/77876442/
"""
