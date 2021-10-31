class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i, num in enumerate(nums):
            if num == i % 10:
                return i
        return -1
    
"""
https://leetcode-cn.com/submissions/detail/233963550/

663 / 663 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB
"""
