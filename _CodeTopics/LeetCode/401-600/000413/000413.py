class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length < 3:
            return 0
        
        res = 0
        for i in range(length-2):
            first, second, third = nums[i], nums[i+1], nums[i+2]
            if second - first != third - second:
                continue
            else:
                res += 1
            j = i + 3
            while j < length and nums[j] - nums[j-1] == second - first:
                res += 1
                j += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/205159724/

15 / 15 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.3 MB

执行用时：12 ms, 在所有 Python 提交中击败了97.25%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了36.26%的用户
"""
