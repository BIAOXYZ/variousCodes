class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
        # 关注下从 12543 到下一个 13245 等例子。

        12345
        12354
        12435
        12453
        12534
        12543

        13245
        13254
        13425
        13452
        13524
        13542
        """

        length = len(nums)
        i, j = length - 2, length - 1

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1            
        if i != -1:
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
"""
https://leetcode-cn.com/submissions/detail/122280289/

265 / 265 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了76.10%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了5.62%的用户
"""
