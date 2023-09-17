class Solution:
    def rob(self, nums: List[int]) -> int:

        # 做两次基本的dp，第一次没有第一个元素，第二次没有最后一个元素。
        ## 基本dp就用最经典也是最简单版本打家劫舍即可。

        # https://leetcode.cn/problems/house-robber/submissions/466748503/?envType=daily-question&envId=2023-09-16
        def basic_rob(nums):
            n = len(nums)
            dp = [nums[0]] + [0] * (n - 1)
            for i in range(1, n):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            return dp[n-1]            

        n = len(nums)
        if n < 3:
            return max(nums)
        return max(basic_rob(nums[1:]), basic_rob(nums[:n-1]))
        
"""
https://leetcode.cn/problems/house-robber-ii/submissions/467182643/?envType=daily-question&envId=2023-09-17

时间
详情
40ms
击败 79.36%使用 Python3 的用户
内存
详情
15.52MB
击败 91.65%使用 Python3 的用户
"""
