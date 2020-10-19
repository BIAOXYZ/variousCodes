class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        """
        思想：看样子应该就是用dp，然后想了想状态转移方程应该是
        dp[i][j] = dp[i-1][j] + dp[i][j-1]。
        此外有个比较特殊的点就是，如果某个位置ij是1，那么这个位置的dp[i][j]就等于0。
        """

        if not obstacleGrid:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for i in range(cols)] for j in range(rows)]
        ##print dp

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[rows-1][cols-1]
        
"""
https://leetcode-cn.com/submissions/detail/85156327/

25 / 41 个通过测试用例
状态：解答错误

输入：[[1,0]]
输出：1
预期：0
"""
