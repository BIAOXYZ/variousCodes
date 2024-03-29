class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 这个 n &= n - 1 的位运算技巧之前也出现过不止一次了！
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/158122422/

601 / 601 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.8 MB

执行用时：20 ms, 在所有 Python 提交中击败了57.14%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了93.96%的用户
"""
