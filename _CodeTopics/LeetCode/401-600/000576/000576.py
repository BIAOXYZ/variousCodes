class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """

        MOD = 10**9 + 7
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # 都忘了这个是不是第一次三维dp，应该不是第一次，但是前面做三维dp也不多就是了。
        dp = [[[0 for col in range(n)] for row in range(m)] for move in range(maxMove+1)]
        dp[0][startRow][startColumn] = 1
        res = 0

        for move in range(maxMove):
            for row in range(m):
                for col in range(n):
                    for direct in directions:
                        nextRow, nextCol = row + direct[0], col + direct[1]
                        if 0 <= nextRow < m and 0 <= nextCol < n:
                            dp[move+1][nextRow][nextCol] = (dp[move+1][nextRow][nextCol] + dp[move][row][col]) % MOD
                        else:
                            res = (res + dp[move][row][col]) % MOD
        return res
        
"""
https://leetcode-cn.com/submissions/detail/207252927/

94 / 94 个通过测试用例
状态：通过
执行用时: 320 ms
内存消耗: 14.7 MB

执行用时：320 ms, 在所有 Python 提交中击败了25.00%的用户
内存消耗：14.7 MB, 在所有 Python 提交中击败了79.17%的用户
"""
