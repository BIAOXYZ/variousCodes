class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 然后轮到（自底向上的）动态规划了。

        small, large = 0, 1
        if n == 0: return small
        elif n == 1: return large

        for i in range(2, n+1):
            res = large + small
            small = large
            large = res
        return res
        
"""
https://leetcode-cn.com/submissions/detail/135725597/

31 / 31 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.9 MB

执行用时：16 ms, 在所有 Python 提交中击败了79.54%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了66.67%的用户
"""
