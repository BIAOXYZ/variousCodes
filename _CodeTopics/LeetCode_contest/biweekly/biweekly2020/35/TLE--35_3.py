class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        
        sum, length = 0, len(nums)
        for i in range(length):
            sum += nums[i]
        if sum % p == 0:
            return 0
        
        dp = [[sum for _ in range(length+1)] for _ in range(length+1)]
        for i in range(length):
            dp[i][i+1] = sum - nums[i]
            if dp[i][i+1] % p == 0:
                return 1
        
        for subArrLen in range(2, length-1):
            for start in range(length-subArrLen+1):
                end = start + subArrLen
                dp[start][end] = dp[start][end-1] - nums[end-1]
                if dp[start][end] % p == 0:
                    return subArrLen
        return -1
    
"""
https://leetcode-cn.com/submissions/detail/109651004/

127 / 142 个通过测试用例
状态：超出时间限制
"""
