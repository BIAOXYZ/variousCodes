class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        if length == 1:
            return 0
        
        res = 0
        for i in range(1, length):
            if nums[i] > nums[i-1]:
                continue
            delta = abs(nums[i] - nums[i-1]) + 1
            nums[i] += delta
            res += delta
        return res
    
"""
https://leetcode-cn.com/submissions/detail/169039629/

94 / 94 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13.4 MB
"""
