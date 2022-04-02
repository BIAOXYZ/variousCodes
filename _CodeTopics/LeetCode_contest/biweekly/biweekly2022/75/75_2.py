class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        while n > 1:
            nextNums = [0] * (n-1)
            for i in range(n-1):
                nextNums[i] = (nums[i] + nums[i+1]) % 10
            nums = nextNums
            n -= 1
        return nums[0]
    
"""
https://leetcode-cn.com/submissions/detail/293854251/

300 / 300 个通过测试用例
状态：通过
执行用时: 1532 ms
内存消耗: 13.3 MB
"""
