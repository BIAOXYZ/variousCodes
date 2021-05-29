class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 用与 1 的 & 运算和移位代替模运算和除法。

        if n <= 0:
            return False
        while n > 1:
            if n & 1 != 0:
                return False
            n >>= 1
        return True
        
"""
https://leetcode-cn.com/submissions/detail/182049634/

1108 / 1108 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB

执行用时：20 ms, 在所有 Python 提交中击败了92.96%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了6.04%的用户
"""
