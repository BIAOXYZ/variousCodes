class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)

        left = [1]*length
        for i in range(1, length):
            left[i] = left[i-1] * nums[i-1]
        
        right = [1 for i in range(length)]
        for j in range(length-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]

        res = []
        for k in range(length):
            res.append(left[k] * right[k])
        return res
        
"""
# https://leetcode-cn.com/submissions/detail/76353904/

18 / 18 个通过测试用例
	状态：通过
执行用时：48 ms
内存消耗：22.3 MB
"""
