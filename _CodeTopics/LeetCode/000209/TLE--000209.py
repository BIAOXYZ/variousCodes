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
            if nums[i] >= s:
                return 1
            for j in range(i+1, length):
                if sumFromTo(nums,i,j) < s:
                    continue
                else:
                    res = min(res, j-i+1)
                    break
        return res

"""
https://leetcode-cn.com/submissions/detail/82795426/

14 / 15 个通过测试用例
状态：超出时间限制

最后执行的输入：120331635
              [29969,14882,18253,28569,4998,34473,9644,3169,25692,18549,22505,24905,1040,14359,6633,38420,2510,8480,8538,5182,...
"""
