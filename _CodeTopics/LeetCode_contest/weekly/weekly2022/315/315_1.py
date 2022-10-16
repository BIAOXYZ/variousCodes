class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        se = set(nums)
        nums.sort(reverse=True)
        for num in nums:
            if num < 0:
                return -1
            if num * (-1) in se:
                return num
        return -1
    
"""
https://leetcode.cn/submissions/detail/373417597/

337 / 337 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.4 MB
"""
