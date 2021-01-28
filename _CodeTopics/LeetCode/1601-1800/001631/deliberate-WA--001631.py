class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        # 先用最普通的二维dp，结果后来发现对于输入
        # [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
        # 本来结果应该是0，这代码却是1。原因是因为顺序不是一定得是自上而下，自左至右，也可以反过来。
        # 所以其实不是dp，而是dfs。不过既然写出来了，也提交下吧。。。

        rows, cols = len(heights), len(heights[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j > 0:
                    dp[i][j] = max(dp[i][j-1], abs(heights[i][j] - heights[i][j-1]))
                elif j == 0 and i > 0:
                    dp[i][j] = max(dp[i-1][j], abs(heights[i][j] - heights[i-1][j]))
                elif i > 0 and j > 0:
                    horizontal = max(dp[i][j-1], abs(heights[i][j] - heights[i][j-1]))
                    vertical = max(dp[i-1][j], abs(heights[i][j] - heights[i-1][j]))
                    dp[i][j] = min(horizontal, vertical)
        print dp
        return dp[rows-1][cols-1]
        
"""
https://leetcode-cn.com/submissions/detail/141996403/

33 / 75 个通过测试用例
状态：解答错误

输入：
[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
输出：
1
预期：
0
"""
