class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        """
        # 接着就是“自底向上”的动态规划实现。首先是最trivial，最plain的版本：
        # 对这题来说就是，每个可能的格子都存一下的二维版dp。
        """

        dp = [[1 for y in range(n+1)] for x in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 or j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]
        
"""
https://leetcode-cn.com/submissions/detail/129750023/

62 / 62 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.3 MB

执行用时：28 ms, 在所有 Python 提交中击败了14.68%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了5.01%的用户
"""
