import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        def is_square(n):
            if math.sqrt(n) == int(math.sqrt(n)):
                return True
            else:
                return False
        
        # 我感觉基本要超时。。。
        for i in range(int(math.sqrt(c/2)) + 1):
            if is_square(c - i*i):
                return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/172685640/

124 / 124 个通过测试用例
状态：通过
执行用时: 160 ms
内存消耗: 13.9 MB

执行用时：160 ms, 在所有 Python 提交中击败了24.00%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了20.80%的用户
"""
