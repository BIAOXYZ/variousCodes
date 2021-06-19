class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # 官方python3的答案，我之前那个是想复杂了，服了。。。

        N = len(grid)
        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0
                        ans += max(grid[r][c] - nval, 0)
        return ans
        
"""
https://leetcode-cn.com/submissions/detail/188071513/

90 / 90 个通过测试用例
状态：通过
执行用时: 60 ms
内存消耗: 13.2 MB

执行用时：60 ms, 在所有 Python 提交中击败了14.93%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了8.96%的用户
"""
"""
之前我自己那个实现傻了，关键步骤上都有问题，肯定对不了！艹！
"""
