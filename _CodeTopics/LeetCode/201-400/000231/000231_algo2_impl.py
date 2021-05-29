class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 根据 n = n & n - 1 会消除 n 最右边（最低位）的1这个trick（也叫 Brian Kernighan 算法），可以不用循环一步到位。

        # 又从答案里学到了另一个位运算的trick：n & (-n) 为 n 的最右边（最低位）的1加上后面的所有0。具体原因和补码有关，不在这里列了。

        if n <= 0:
            return False
        if n & -n == n:
            return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/182051864/

1108 / 1108 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.3 MB

执行用时：24 ms, 在所有 Python 提交中击败了79.48%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了5.03%的用户
"""
