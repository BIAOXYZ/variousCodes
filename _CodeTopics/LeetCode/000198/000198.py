class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
 
        length = len(nums)
        if length == 0:
            return 0
        elif length <= 2:
            return max(nums)
        
        dp = [0 for i in range(length)]
        # dp[i]表示从数组下标0（也就是最开头）开始到数组下标i为止（包括nums[i]本身），
        # 形成的这个子数组里，按规则隔着偷能达到的最大值。
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, length):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[length-1]
        
"""
https://leetcode-cn.com/submissions/detail/106465470/

69 / 69 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 12.6 MB
"""
"""
执行用时：28 ms, 在所有 Python 提交中击败了9.90%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了79.58%的用户
"""
