class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 1: return 0
        
        for i in range(n-1):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        
        if sum(nums[:n-1]) == 0:
            return n-1
        else:
            return -1
        
"""
https://leetcode-cn.com/submissions/detail/215208223/

294 / 294 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.9 MB
"""
