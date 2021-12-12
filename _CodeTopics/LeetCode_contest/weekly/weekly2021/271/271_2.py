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
            currMax = currMin = nums[i]
            for j in range(i-1, -1, -1):
                currMax = max(currMax, nums[j])
                currMin = min(currMin, nums[j])
                incr += currMax - currMin
            dp[i] = dp[i-1] + incr
        return dp[n-1]
    
"""
https://leetcode-cn.com/submissions/detail/247648046/

71 / 71 个通过测试用例
状态：通过
执行用时: 2032 ms
内存消耗: 13.3 MB
"""
