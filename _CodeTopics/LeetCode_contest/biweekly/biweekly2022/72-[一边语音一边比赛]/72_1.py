class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        res = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j] and i * j % k == 0:
                    res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/270470590/

237 / 237 个通过测试用例
状态：通过
执行用时: 60 ms
内存消耗: 13.2 MB
"""
