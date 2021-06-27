class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        return nums[-1]*nums[-2] - nums[0]*nums[1]
    
"""
https://leetcode-cn.com/submissions/detail/190056280/

96 / 96 个通过测试用例
状态：通过
执行用时: 48 ms
内存消耗: 13.7 MB
"""
