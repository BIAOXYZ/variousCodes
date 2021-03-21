class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        res = currMax = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                currMax += nums[i]
            else:
                res = max(res, currMax)
                currMax = nums[i]
        res = max(res, currMax)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/157773120/

104 / 104 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 12.9 MB
"""
