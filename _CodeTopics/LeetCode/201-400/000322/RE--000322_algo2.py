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
        # dp = [0] + [infinite for i in range(amount)]
        # 这里本来用的是上面那句，但是有问题。比如 coins = [1], amount = 0 时，下面dp数组
        # 初始化赋值的for循环就会报“list index out of range”。所以干脆申请dp数组的时候
        # 申请稍大一点。
        # 另外这里dp数组如果用字典代替的话应该没有这个问题。
        maxdplength = max(max(coins), amount)
        dp = [0] + [infinite for i in range(maxdplength)]
        for coin in coins:
            dp[coin] = 1

        for i in range(1, amount+1):
            if dp[i] == infinite:
                for coin in coins:
                    if i - coin >= 0:
                        dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[amount] if dp[amount] != infinite else -1
        
"""
https://leetcode-cn.com/submissions/detail/121062999/

8 / 182 个通过测试用例
状态：执行出错

执行出错信息：
Line 22: MemoryError
最后执行的输入：
[2147483647]
2
"""
