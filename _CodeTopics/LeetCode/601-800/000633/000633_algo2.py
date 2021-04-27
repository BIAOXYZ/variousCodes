import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        left, right = 0, int(math.sqrt(c))
        while left <= right:
            summ = left * left + right * right
            if summ == c:
                return True
            elif summ < c:
                left += 1
            else:
                right -= 1
        return False
        
"""
https://leetcode-cn.com/submissions/detail/172686643/

124 / 124 个通过测试用例
状态：通过
执行用时: 76 ms
内存消耗: 12.9 MB

执行用时：76 ms, 在所有 Python 提交中击败了88.00%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了70.00%的用户
"""
