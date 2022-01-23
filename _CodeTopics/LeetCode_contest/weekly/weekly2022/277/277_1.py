class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        n = len(nums)
        if len(set(nums)) <= 2:
            return 0
        
        i = 0
        while i < n and nums[i] == nums[0]:
            i += 1
        j = 0
        while n-1-j >= 0 and nums[n-1-j] == nums[-1]:
            j += 1
        return n - i - j
    
"""
https://leetcode-cn.com/submissions/detail/261446098/

127 / 127 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB
"""
