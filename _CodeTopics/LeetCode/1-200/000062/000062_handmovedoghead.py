import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # 手动狗头题。
        return math.factorial(m+n-2) / (math.factorial(m-1) * math.factorial(n-1))
        
"""
https://leetcode-cn.com/submissions/detail/129780892/

62 / 62 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 13.1 MB

执行用时：8 ms, 在所有 Python 提交中击败了99.36%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了11.53%的用户
"""
"""
库函数，永远滴神~
"""
