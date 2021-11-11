class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 参见官方答案吧。。。看题目以为二分查找，没想起来。
        # 1. dp[i][j] 表示数字在 (i,j) 之间需要的最少查找金额，所以最终是为了求 dp[1][n]。
        # 2. 两重 for 循环的顺序为什么是那样还是稍费点思考的。。。

        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                dp[i][j] = min(k + max(dp[i][k - 1], dp[k + 1][j]) for k in range(i, j))
        return dp[1][n]
        
"""
https://leetcode-cn.com/submissions/detail/237839391/

执行用时：1116 ms, 在所有 Python 提交中击败了80.00%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了46.67%的用户
通过测试用例：
27 / 27
"""
