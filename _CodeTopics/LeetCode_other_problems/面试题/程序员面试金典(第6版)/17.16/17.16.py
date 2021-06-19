class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 经典动态规划题。dp[i]表示，可选择的为前i个时，能获得的最大分钟数。

        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        
        dp = [0 for _ in range(length)]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, length):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[length-1]
        
"""
https://leetcode-cn.com/submissions/detail/188039180/

69 / 69 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.2 MB

执行用时：12 ms, 在所有 Python 提交中击败了95.83%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了6.25%的用户
"""
