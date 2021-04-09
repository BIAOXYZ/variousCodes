class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        while n:
            if n % 2 == 0:
                n /= 2
            elif n % 3 == 0:
                n /= 3
            elif n % 5 == 0:
                n /= 5
            else:
                return False if n > 1 else True
        
"""
https://leetcode-cn.com/submissions/detail/165915404/

1013 / 1013 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13 MB

执行用时：32 ms, 在所有 Python 提交中击败了32.04%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了47.54%的用户
"""
