class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n >= 3 and n % 3 == 0:
            n /= 3
        return True if n == 1 else False
        
"""
https://leetcode-cn.com/submissions/detail/222166820/

21038 / 21038 个通过测试用例
状态：通过
执行用时: 184 ms
内存消耗: 13.2 MB

执行用时：184 ms, 在所有 Python 提交中击败了42.36%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了16.01%的用户
"""
