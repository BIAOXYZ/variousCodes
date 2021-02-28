class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.nums:
            return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

"""
https://leetcode-cn.com/submissions/detail/149625974/

16 / 16 个通过测试用例
状态：通过
执行用时: 568 ms
内存消耗: 16.5 MB

执行用时：568 ms, 在所有 Python 提交中击败了40.65%的用户
内存消耗：16.5 MB, 在所有 Python 提交中击败了92.28%的用户
"""
