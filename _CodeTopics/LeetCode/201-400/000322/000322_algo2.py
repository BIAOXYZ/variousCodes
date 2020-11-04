class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        """
        # 动态规划方法。
        # 注意动态规划是“自底向上”的，也就是从小的格子一点点往上，直到达到amout的格子
        # 而记忆化搜索是上来就从amout开始，“自顶向下”一点点拆。
        """

        infinite = float('inf')
        dp = [0] + [infinite for i in range(amount)]
        """
        # 后来因为那个MemoryError的RE问题，发现了这里其实不用初始化。
        for coin in coins:
            dp[coin] = 1
        """

        for i in range(1, amount+1):
            if dp[i] == infinite:
                for coin in coins:
                    if i - coin >= 0:
                        dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[amount] if dp[amount] != infinite else -1
        
"""
https://leetcode-cn.com/submissions/detail/121070095/

182 / 182 个通过测试用例
状态：通过
执行用时: 948 ms
内存消耗: 13.6 MB

执行用时：948 ms, 在所有 Python 提交中击败了56.13%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了16.42%的用户
"""
