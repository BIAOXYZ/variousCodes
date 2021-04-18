class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length < 2:
            return length
        
        slow, fast = 0, 1
        while fast < length:
            if nums[fast] != nums[slow]:
                nums[slow+1] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        return slow + 1
        
"""
https://leetcode-cn.com/submissions/detail/169226246/

161 / 161 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 14.2 MB

执行用时：32 ms, 在所有 Python 提交中击败了49.26%的用户
内存消耗：14.2 MB, 在所有 Python 提交中击败了82.29%的用户
"""
