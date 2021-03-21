class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0
        for i in range(32):
            if n & (1 << i) > 0:
                res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/158118647/

601 / 601 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB

执行用时：16 ms, 在所有 Python 提交中击败了79.06%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了57.52%的用户
"""
