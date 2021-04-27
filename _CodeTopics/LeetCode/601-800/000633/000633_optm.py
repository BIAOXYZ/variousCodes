import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        a = 0
        while a * a <= c:
            b = math.sqrt(c - a*a)
            if b == int(b):
                return True
            a += 1
        return False
        
"""
https://leetcode-cn.com/submissions/detail/172685996/

124 / 124 个通过测试用例
状态：通过
执行用时: 156 ms
内存消耗: 12.9 MB

执行用时：156 ms, 在所有 Python 提交中击败了26.40%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了79.60%的用户
"""
