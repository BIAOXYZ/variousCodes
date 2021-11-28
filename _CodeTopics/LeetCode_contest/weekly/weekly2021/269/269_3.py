class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 1 or n == 2:
            return n
        
        minind = nums.index(min(nums))
        maxind = nums.index(max(nums))
        small, big = min(minind, maxind), max(minind, maxind)
        return min(big+1, n-small, small+1+n-big)
    
"""
https://leetcode-cn.com/submissions/detail/243010519/

60 / 60 个通过测试用例
状态：通过
执行用时: 72 ms
内存消耗: 20.8 MB
"""
