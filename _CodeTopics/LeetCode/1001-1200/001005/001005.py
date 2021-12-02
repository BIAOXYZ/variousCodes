class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        length = len(nums)
        nums.sort()
        i = 0
        while i < length and nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1
        
        if k == 0:
            return sum(nums)
        elif k % 2 == 0:
            return sum(nums)
        else:
            return sum(nums) - min(nums) * 2
        
"""
https://leetcode-cn.com/submissions/detail/244731435/

执行用时：20 ms, 在所有 Python 提交中击败了76.67%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了28.89%的用户
通过测试用例：
80 / 80
"""
