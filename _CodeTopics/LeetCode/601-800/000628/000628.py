class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        if nums[0] >= 0 or nums[-1] <= 0:
            return nums[-1] * nums[-2] * nums[-3]
        elif nums[1] >= 0:
            return nums[-1] * nums[-2] * nums[-3]
        else:
            return nums[-1] * max(nums[0] * nums[1], nums[-2] * nums[-3])
        
"""
https://leetcode-cn.com/submissions/detail/139679987/

91 / 91 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 14.1 MB

执行用时：56 ms, 在所有 Python 提交中击败了76.43%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了17.20%的用户
"""
