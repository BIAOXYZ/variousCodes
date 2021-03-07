class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        
        diff = abs(goal - sum(nums))
        return diff/limit + int(bool(diff%limit))
    
"""
https://leetcode-cn.com/submissions/detail/151995578/

75 / 75 个通过测试用例
状态：通过
执行用时: 56 ms
内存消耗: 19.8 MB
"""
