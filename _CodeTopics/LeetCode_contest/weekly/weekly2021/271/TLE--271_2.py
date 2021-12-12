class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 1:
            return 0
        
        dp = [0] * n
        dp[0] = 0
        dp[1] = abs(nums[1] - nums[0])
        for i in range(2, n):
            incr = 0
            for j in range(i-1, -1, -1):
                incr += max(nums[j:i+1]) - min(nums[j:i+1])
            dp[i] = dp[i-1] + incr
        return dp[n-1]
    
"""
https://leetcode-cn.com/submissions/detail/247642709/

39 / 71 个通过测试用例
状态：超出时间限制
"""
