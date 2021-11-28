class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        n = len(nums)
        res = [-1] * n
        if n < 2*k + 1:
            return res
        
        wd = sum(nums[:2*k+1])
        res[k] = wd / (2*k+1)
        for i in range(k+1, n-k):
            wd = wd - nums[i-k-1] + nums[i+k]
            res[i] = wd / (2*k+1)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/243005774/

36 / 36 个通过测试用例
状态：通过
执行用时: 192 ms
内存消耗: 32.8 MB
"""
