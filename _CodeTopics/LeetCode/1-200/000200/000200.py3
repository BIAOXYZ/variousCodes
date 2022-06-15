class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(grid), len(grid[0])
        def is_legal_coordinate(x, y):
            return 0 <= x < m and 0 <= y < n

        visited = set()
        def dfs(coor):
            x, y = coor
            if coor in visited or grid[x][y] == '0':
                return
            visited.add(coor)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_legal_coordinate(nx, ny):
                    dfs((nx, ny))
        
        res = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == '1':
                    res += 1
                    dfs((i, j))
        return res
        
"""
https://leetcode.cn/submissions/detail/325730423/

执行用时：
180 ms
, 在所有 Python3 提交中击败了
10.84%
的用户
内存消耗：
34.2 MB
, 在所有 Python3 提交中击败了
5.02%
的用户
通过测试用例：
49 / 49
"""
