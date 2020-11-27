class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 这题是困难，所以都不用问，暴力肯定超时。。。
        
        if not nums:
            return 0
        
        res = 0
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] > 2 * nums[j]:
                    res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/126806185/

33 / 137 个通过测试用例
状态：超出时间限制
"""
