class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        res = [-1] * n
        for i in range(n):
            res[i] = nums[nums[i]]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/192094213/

134 / 134 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13.1 MB
"""
