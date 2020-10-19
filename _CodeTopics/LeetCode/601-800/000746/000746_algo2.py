class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        length = len(cost)
        dp = [0 for i in range(length)]
        # dp[i]表示，踩着（或者说“恰好从”、“恰好到达并经过”）第i个台阶往上走时的最小花费。
        # 所以，踩着第0个台阶向上走时，最小花费是cost[0]（因为一开始就可以站上去）；
        # 同理，踩着第1个台阶向上走时，最小花费是cost[1]（也是因为一开始就可以站上去）。
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, length):
            # 那么递推公式其实就是：从第i-1台阶恰好踩着i和从第i-2台阶出发恰好踩着i，两者中的较小者。
            dp[i] = min(dp[i-1], dp[i-2]) +  cost[i]
        # 最后为了到达那个虚拟的顶部，可以从length-1跨一步，也可以从length-2跨两步。
        #（跨这一步或两步可以认为不计消耗，因为已经算在dp项里了）。
        return min(dp[length-1], dp[length-2])
        
"""
https://leetcode-cn.com/submissions/detail/106498377/

276 / 276 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 12.7 MB
"""
"""
执行用时：52 ms, 在所有 Python 提交中击败了33.26%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了80.93%的用户
"""
