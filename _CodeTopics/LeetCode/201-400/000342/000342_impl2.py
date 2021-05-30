class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 用与 3 的 & 运算和移位代替模运算和除法。
        # 这次把 3 用二进制形式写得更清楚点。也是参考了答案里的 n & 0xaaaaaaaa 才想到的。

        if n <= 0:
            return False
        while n >= 4:
            ### if n & 3 != 0:
            if n & 0b11 != 0:
                return False
            n >>= 2
        return True if n == 1 else False
        
"""
https://leetcode-cn.com/submissions/detail/182352473/

1061 / 1061 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.2 MB

执行用时：16 ms, 在所有 Python 提交中击败了98.21%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.36%的用户
"""
