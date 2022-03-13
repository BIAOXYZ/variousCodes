class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        
        n = len(nums)
        res = set()
        for i in range(n):
            if nums[i] == key:
                for j in range(max(0, i-k), min(i+k+1, n)):
                    res.add(j)
        return sorted(list(res))
    
"""
https://leetcode-cn.com/submissions/detail/282139362/

83 / 83 个通过测试用例
状态：通过
执行用时: 300 ms
内存消耗: 13.2 MB
"""
