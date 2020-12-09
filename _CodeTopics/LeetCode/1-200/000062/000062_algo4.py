class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # 手动计算组合数 $C_{m+n-2}^{m-1}$ 的实现。

        dividend = m + n -2
        divisor = 1
        res = 1
        for i in range(m-1):
            res = res * dividend / divisor
            dividend -= 1
            divisor += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/129875613/

62 / 62 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.1 MB

执行用时：28 ms, 在所有 Python 提交中击败了14.68%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了8.16%的用户
"""
