class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
 
        def sumFromTo(nums, start=0, end=len(nums)-1):
            summation = 0
            for i in range(start, end+1):
                summation += nums[i]
            return summation
        
        length = len(nums)
        if length == 0 or sumFromTo(nums) < s:
            return 0
        res = length

        for i in range(length-1):
            for j in range(i+1, length):
                if sumFromTo(nums,i,j) < s:
                    continue
                else:
                    res = min(res, j-i+1)
                    break
        return res
        
"""
https://leetcode-cn.com/submissions/detail/82776077/

12 / 15 个通过测试用例
状态：解答错误

输入：4
     [1,4,4]
输出：2
预期：1
"""
