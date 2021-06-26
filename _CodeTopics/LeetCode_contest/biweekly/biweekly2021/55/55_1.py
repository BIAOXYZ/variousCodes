class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        flag = 0
        n = len(nums)
        prev = nums[0]
        for i in range(1, n):
            if nums[i] <= prev:
                flag += 1 
                if flag > 1:
                    return False
                if i - 2 >= 0 and nums[i] <= nums[i-2]:
                    prev = nums[i-1]
                else:
                    prev = nums[i]
            else:
                prev = nums[i]
        return True
    
"""
https://leetcode-cn.com/submissions/detail/189978981/

105 / 105 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.9 MB
"""
