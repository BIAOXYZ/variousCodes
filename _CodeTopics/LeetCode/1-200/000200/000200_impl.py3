class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # 不使用 visited，而是直接把图里的 1 变成 0。

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(grid), len(grid[0])
        def is_legal_coordinate(x, y):
            return 0 <= x < m and 0 <= y < n

        def dfs(coor):
            x, y = coor
            if grid[x][y] == '0':
                return
            grid[x][y] = '0'
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_legal_coordinate(nx, ny):
                    dfs((nx, ny))
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs((i, j))
        return res
        
"""
https://leetcode.cn/submissions/detail/326109166/

执行用时：
148 ms
, 在所有 Python3 提交中击败了
23.64%
的用户
内存消耗：
24 MB
, 在所有 Python3 提交中击败了
36.90%
的用户
通过测试用例：
49 / 49
"""
