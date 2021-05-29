class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 先用最trivial的。

        if n <= 0:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n /= 2
        return True
        
"""
https://leetcode-cn.com/submissions/detail/182048747/

1108 / 1108 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB

执行用时：16 ms, 在所有 Python 提交中击败了98.21%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了45.53%的用户
"""
