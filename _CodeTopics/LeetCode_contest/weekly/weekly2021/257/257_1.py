class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        res = 0
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/215306858/

211 / 211 个通过测试用例
状态：通过
执行用时: 848 ms
内存消耗: 13.3 MB
"""
