MASK1 = 4294967296  # 2^32
MASK2 = 2147483648  # 2^31
MASK3 = 2147483647  # 2^31-1

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        # 官方答案解法，主要是一会准备故意写个错的，试试没有这些 MASK 会怎样。

        while b != 0:
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            b = carry
        if a & MASK2:  # 负数
            return ~((a ^ MASK2) ^ MASK3)
        else:  # 正数
            return a
        
"""
https://leetcode-cn.com/submissions/detail/223226986/

13 / 13 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13 MB

执行用时：12 ms, 在所有 Python 提交中击败了92.16%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了50.00%的用户
"""
