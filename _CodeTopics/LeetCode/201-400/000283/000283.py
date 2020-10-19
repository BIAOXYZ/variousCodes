class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        numofzero = 0

        for i in range(length):
            if nums[i] == 0:
                numofzero += 1
                nums[i] = None
        while None in nums:
            nums.pop(nums.index(None))
        for i in range(numofzero):
            nums.append(0)
        return nums
        
"""
https://leetcode-cn.com/submissions/detail/77884665/

21 / 21 个通过测试用例
状态：通过
执行用时：108 ms
内存消耗：13.9 MB
"""
