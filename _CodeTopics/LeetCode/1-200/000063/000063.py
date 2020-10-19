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

        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for i in range(cols)] for j in range(rows)]
        ##print dp

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    continue
                # [[0,0],[1,1],[0,0]] 这个用例第二行堵死了，但是第三行dp[2][0]还是会赋值成1，
                # 肯定不对。想了想干脆分开写，不然到底是i-1还是j-1不好区分。
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0 and i != 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[rows-1][cols-1]
        
"""
https://leetcode-cn.com/submissions/detail/85162194/

41 / 41 个通过测试用例
状态：通过
执行用时：16 ms
内存消耗：12.6 MB
"""
"""
# 把时间和空间消耗都贴一下，因为可能会写一个利用「滚动数组思想」优化空间复杂度的实现。

执行用时：16 ms, 在所有 Python 提交中击败了92.23%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了16.67%的用户
"""
