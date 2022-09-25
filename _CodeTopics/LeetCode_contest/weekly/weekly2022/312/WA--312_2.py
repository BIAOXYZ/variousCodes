class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxElem = max(nums)
        n = len(nums)
        res = 1
        pos = -1 
        for i in range(n):
            if pos == -1:
                if nums[i] == maxElem:
                    pos = i
            elif pos >= 0:
                if nums[i] != maxElem:
                    res = max(res, i - pos)
                    pos = -1
        return res
    
"""
https://leetcode.cn/submissions/detail/366898866/

46 / 50 个通过测试用例
状态：解答错误

输入：
[378034,378034,378034]
输出：
1
预期：
3
"""
