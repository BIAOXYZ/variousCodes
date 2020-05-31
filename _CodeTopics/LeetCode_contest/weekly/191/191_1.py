class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        if length == 2:
            return (nums[0]-1)*(nums[1]-1)
        
        Max = max(nums)
        ind = nums.index(Max)
        nums.pop(ind)
        Max2 = max(nums)
        return (Max-1)*(Max2-1)
    
"""
# https://leetcode-cn.com/submissions/detail/75071505/

103 / 103 个通过测试用例
	状态：通过
执行用时：12 ms
内存消耗：12.7 MB
"""
