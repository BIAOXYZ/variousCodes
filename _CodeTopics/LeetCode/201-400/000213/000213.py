class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length <= 3:
            return max(nums)
        
        # 这个dp里的每个元素是一个由两个整数构成的数组：
        # 每个数组第一个元素表示可能有 nums[0] 参与的时候（也就是对nums[0]是否参与不设限制），以该坐标结尾的最大值；
        # 每个数组第二个元素表示没有 nums[0] 参与的时候，以该坐标结尾的最大值。
        # 之所以要这么做就是因为整体是一个环形，到最后 length-1 处时必须得清楚前面那些dp值到底有没有nums[0]。
        dp = [[-1, -1] for _ in range(length)]
        dp[0] = [nums[0], 0]
        dp[1] = [max(nums[0], nums[1]), nums[1]]

        for i in range(2, length):
            dp[i][0] = max(dp[i-1][0], dp[i-2][0] + nums[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][1] + nums[i])
        dp[length-1][0] = max(dp[length-2][0], dp[length-3][0])
        dp[length-1][1] = max(dp[length-2][1], dp[length-3][1] + nums[i])
        return max(dp[length-1])
        
"""
https://leetcode-cn.com/submissions/detail/168007317/

74 / 74 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.1 MB

执行用时：16 ms, 在所有 Python 提交中击败了84.37%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了8.62%的用户
"""
