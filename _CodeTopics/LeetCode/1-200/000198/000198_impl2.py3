class Solution:
    def rob(self, nums: List[int]) -> int:

        # 今天（20230916）在朋友圈发了正式的结婚请帖～
        
        n = len(nums)
        dp = [nums[0]] + [0] * (n - 1)
        for i in range(1, n):
            # Python语言的特性可以做到这个写法也是对的，因为当 i = 1 时，
            ## dp[i-1] 的实质是 dp[-1]，此时的值为 0。
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[n-1]
        
"""
https://leetcode.cn/problems/house-robber/submissions/466748503/?envType=daily-question&envId=2023-09-16

时间
详情
44ms
击败 56.80%使用 Python3 的用户
内存
详情
15.26MB
击败 99.89%使用 Python3 的用户
"""
