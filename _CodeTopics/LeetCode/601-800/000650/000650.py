class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [i for i in range(n+1)]
        dp[1] = 0

        def factorization_of_le_1000(k):
            res = [1, k]
            # 32**2 = 1024 已经超过 1000 了，所以最多到 31。
            for i in range(2, min(32, k)):
                if k % i == 0:
                    res.append(i)
                    res.append(k/i)
            return res

        # 注意看题，最开始就理解错了。
        # 1. 如果是素数，那么只能是需要 n 次。
        # 2. 如果是合数，那么应该是根据 n 的各个因子 i 对应的 dp[i] 来计算。
        for k in range(2, n+1):
            factors = factorization_of_le_1000(k)
            if len(factors) == 2:
                dp[k] = k
            else:
                for i in range(2, len(factors)):
                    factor = factors[i]
                    dp[k] = min(dp[k], dp[factor] + k / factor)
        return dp[n]
        
"""
https://leetcode-cn.com/submissions/detail/221045630/

126 / 126 个通过测试用例
状态：通过
执行用时: 112 ms
内存消耗: 13.3 MB

执行用时：112 ms, 在所有 Python 提交中击败了49.25%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了10.45%的用户
"""
