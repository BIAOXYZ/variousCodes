class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 随便贴个（不可能是最大值的）负数进去，这样不用最后再处理一次。
        nums.append(-1)
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
https://leetcode.cn/submissions/detail/366900918/

50 / 50 个通过测试用例
状态：通过
执行用时: 76 ms
内存消耗: 21.9 MB
"""
