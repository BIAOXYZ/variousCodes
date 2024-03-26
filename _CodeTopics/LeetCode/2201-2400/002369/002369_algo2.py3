class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        def is_legal_subarray(lis):
            n = len(lis)
            if n == 2:
                if lis[0] == lis[1]:
                    return True
            elif n == 3:
                if lis[0] == lis[1] == lis[2]:
                    return True
                if lis[1] == lis[0] + 1 and lis[2] == lis[1] + 1:
                    return True
            return False

        n = len(nums)
        dp = [0] * n
        for i in range(n-1, -1, -1):
            if i == n-1:
                dp[i] = False
            elif i == n-2 or i == n-3:
                dp[i] = is_legal_subarray(nums[i:])
            else:
                dp[i] = (is_legal_subarray(nums[i:i+2]) and dp[i+2]) or \
                    (is_legal_subarray(nums[i:i+3]) and dp[i+3])
        return dp[0]
        
"""
https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/submissions/516957392?envType=daily-question&envId=2024-03-01

通过
提交于 2024.03.26 21:02

执行用时分布
307
ms
击败
5.05%
使用 Python3 的用户
消耗内存分布
30.84
MB
击败
66.77%
使用 Python3 的用户
"""
