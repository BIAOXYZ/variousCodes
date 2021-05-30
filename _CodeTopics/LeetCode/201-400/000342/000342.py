class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        while n >= 4:
            if n % 4 != 0:
                return False
            n /= 4
        return True if n == 1 else False
        
"""
https://leetcode-cn.com/submissions/detail/182349958/

1061 / 1061 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 12.9 MB

执行用时：28 ms, 在所有 Python 提交中击败了52.38%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了57.74%的用户
"""
