class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        n = len(nums)
        summation = sum(nums)
        dp = [0 for _ in range(n)]
        dp[0] = sum(i * nums[i] for i in range(n))
        for i in range(1, n):
            posToBecomeZero = n - i
            # 除了 posToBecomeZero 分界点上的数 nums[posToBecomeZero] 外每个数都会多一次；
            # 此外，nums[posToBecomeZero] 从最后一位移到第一位，还需要再减去 n-1 次。
            dp[i] = dp[i-1] + (summation - nums[posToBecomeZero]) - nums[posToBecomeZero] * (n-1)
        return max(dp)
        
"""
https://leetcode-cn.com/submissions/detail/303679639/

执行用时：
404 ms
, 在所有 Python3 提交中击败了
19.92%
的用户
内存消耗：
24.1 MB
, 在所有 Python3 提交中击败了
31.04%
的用户
通过测试用例：
58 / 58
"""
