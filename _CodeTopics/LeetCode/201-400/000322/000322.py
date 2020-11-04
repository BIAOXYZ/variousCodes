class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # 记忆化搜索。虽然结果对，但是好像运行起来比较慢，不知道会不会超时。。。
        def memorize_search(amount):
            if dic.has_key(amount):
                return dic[amount]
            dic[amount] = MAXINT
            for coin in coins:
                if amount - coin >= 0:
                    dic[amount] = min(dic[amount], 1 + memorize_search(amount-coin))
            return dic[amount]
        
        # 也就是 sys.maxint
        MAXINT = 9223372036854775807
        dic = {0:0}
        for coin in coins:
            dic[coin] = 1
        
        memorize_search(amount)
        return dic[amount] if dic[amount] != MAXINT else -1
        
"""
https://leetcode-cn.com/submissions/detail/121048646/

182 / 182 个通过测试用例
状态：通过
执行用时: 1692 ms
内存消耗: 45.7 MB

执行用时：1692 ms, 在所有 Python 提交中击败了6.34%的用户
内存消耗：45.7 MB, 在所有 Python 提交中击败了5.03%的用户
"""
