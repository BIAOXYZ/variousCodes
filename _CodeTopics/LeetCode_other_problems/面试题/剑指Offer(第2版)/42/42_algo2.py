class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        dp = [nums[0]] + [0 for i in range(length-1)]

        for i in range(1, length):
            if dp[i-1] >= 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
        
"""
https://leetcode-cn.com/submissions/detail/196868564/

202 / 202 个通过测试用例
状态：通过
执行用时: 44 ms
内存消耗: 21.1 MB

执行用时：44 ms, 在所有 Python 提交中击败了73.14%的用户
内存消耗：21.1 MB, 在所有 Python 提交中击败了5.06%的用户
"""
