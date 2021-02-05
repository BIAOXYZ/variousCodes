class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """

        # 动态规划版本。思路是：用一个二维数组来存储已经计算出来的左右两边的和。该二维数组的
        # 第i行第j列代表从左边选i个数和右边选j个数。注意一下index别搞错就行，可能会有些小坑。

        dp = [[0 for i in range(k+1)] for j in range(k+1)]
        res = 0

        for row in range(k+1):
            for col in range(k+1-row):
                if col != 0:
                    dp[row][col] = dp[row][col-1] + cardPoints[-col]
                elif row != 0:
                    dp[row][col] = dp[row-1][col] + cardPoints[row-1]
                else:
                    continue
                if row + col == k:
                    res = max(res, dp[row][col])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/144072754/

31 / 40 个通过测试用例
状态：超出时间限制
"""
"""
dp都超时？？？
"""
