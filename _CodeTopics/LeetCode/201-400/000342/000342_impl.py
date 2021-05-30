class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 用与 3 的 & 运算和移位代替模运算和除法。

        if n <= 0:
            return False
        while n >= 4:
            if n & 3 != 0:
                return False
            n >>= 2
        return True if n == 1 else False
        
"""
https://leetcode-cn.com/submissions/detail/182352012/

1061 / 1061 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13 MB

执行用时：32 ms, 在所有 Python 提交中击败了31.55%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了26.19%的用户
"""
