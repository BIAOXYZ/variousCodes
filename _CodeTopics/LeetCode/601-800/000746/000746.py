class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        length = len(cost)
        dp = [0 for i in range(length)]
        dp[0], dp[1] = 0, min(cost[0], cost[1])

        for i in range(2, length):
            # 这题目描述腊鸡死了。。。。
            dp[i] = min(cost[i] + dp[i-1], cost[i-1] + dp[i-2])
        return dp[length-1]
        
"""
https://leetcode-cn.com/submissions/detail/106477266/

276 / 276 个通过测试用例
状态：通过
执行用时: 48 ms
内存消耗: 12.9 MB
"""
"""
执行用时：48 ms, 在所有 Python 提交中击败了53.72%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了25.77%的用户
"""
