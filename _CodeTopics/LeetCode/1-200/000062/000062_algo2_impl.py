class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        """
        # 依然是二维dp，不过这次之前那个版本 `000062_algo2.py` 行和列都多申请了一维。
        # 这次是不用多申请的版本。写完对比下 `000062_algo2.py` 发现写法上也是更简单的。
        """

        dp = [[1 for y in range(n)] for x in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        
"""
https://leetcode-cn.com/submissions/detail/129774929/

62 / 62 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB

执行用时：24 ms, 在所有 Python 提交中击败了36.55%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了27.97%的用户
"""
