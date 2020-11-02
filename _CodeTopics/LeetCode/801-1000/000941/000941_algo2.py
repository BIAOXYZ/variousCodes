class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        length = len(A)
        if length < 3:
            return False

        left, right = 0, length - 1
        while left <= length - 3 and A[left] < A[left+1]:
            left += 1
        while right >= 2 and A[right] < A[right-1]:
            right -= 1
        return left == right
        
"""
https://leetcode-cn.com/submissions/detail/120535144/

51 / 51 个通过测试用例
状态：通过
执行用时: 180 ms
内存消耗: 14.4 MB

执行用时：180 ms, 在所有 Python 提交中击败了92.17%的用户
内存消耗：14.4 MB, 在所有 Python 提交中击败了7.41%的用户
"""
