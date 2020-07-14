class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        # 从试运行的结果看，这分支没用，也就是题目压根就没考虑empty list。
        """
        [[-2,-3,3],[-5,-10,1],[10,30,-5]]
        [[-1]]
        []
        """
        if not dungeon:
            return

        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        ##print dp

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if i == rows-1 and j == cols-1:
                    # 假设最右下角格子值为-3，那么此时应该是1-(-3)=4；但是如果值是3话，
                    # 1-3=-2，可是骑士进这个格子至少得有1滴血吧，所以得用max函数这样求一下，
                    # 区分一下格子的值的情况。
                    dp[i][j] = max(1 - dungeon[rows-1][cols-1], 1)
                elif i == rows - 1 and j != cols-1:
                    dp[i][j] = max(dp[i][j+1] - dungeon[i][j], 1)
                elif i != rows - 1 and j == cols-1:
                    dp[i][j] = max(dp[i+1][j] - dungeon[i][j], 1)
                else:
                    dp[i][j] = max(min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j], 1)
        return dp[0][0]
        
"""
https://leetcode-cn.com/submissions/detail/87848883/

45 / 45 个通过测试用例
状态：通过
执行用时：32 ms
内存消耗：13.2 MB
"""
"""
执行用时：32 ms, 在所有 Python 提交中击败了71.56%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了100.00%的用户
"""
