class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 根据 n = n & n - 1 会消除 n 最右边（最低位）的1这个trick（也叫 Brian Kernighan 算法），可以不用循环一步到位。

        if n <= 0:
            return False
        if n & n - 1 != 0:
            return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/182050673/

1108 / 1108 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13 MB

执行用时：32 ms, 在所有 Python 提交中击败了32.80%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了31.59%的用户
"""
"""
只是我没懂，明明都不需要循环，为啥这个还更慢。。。
猜测是 n & n-1 实质上要走遍 n 的每一位，while循环也一样要走这么多位，在异或运算上复杂度相等。但是这个看起来快的算法，反而要算一下 n - 1。
"""
