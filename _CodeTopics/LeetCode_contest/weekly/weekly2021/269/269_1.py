class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if num == target:
                res.append(i)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/242996587/

216 / 216 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.9 MB
"""
