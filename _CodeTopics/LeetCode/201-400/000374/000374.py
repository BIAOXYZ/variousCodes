# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1
        
"""
https://leetcode-cn.com/submissions/detail/186535132/

25 / 25 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.1 MB

执行用时：12 ms, 在所有 Python 提交中击败了93.23%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了17.54%的用户
"""
