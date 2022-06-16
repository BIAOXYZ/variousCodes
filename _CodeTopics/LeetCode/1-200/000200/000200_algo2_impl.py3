from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # BFS 版本的不使用 visited，而是直接把图里的 1 变成 0。

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(grid), len(grid[0])
        def is_legal_coordinate(x, y):
            return 0 <= x < m and 0 <= y < n
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    stk = deque()
                    stk.append((i, j))
                    while stk:
                        cur = stk.popleft()
                        x, y = cur
                        if grid[x][y] == '0':
                            continue
                        grid[x][y] = '0'
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if is_legal_coordinate(nx, ny):
                                stk.append((nx, ny))
        return res
        
"""
https://leetcode.cn/submissions/detail/326109894/

执行用时：
144 ms
, 在所有 Python3 提交中击败了
26.79%
的用户
内存消耗：
23.9 MB
, 在所有 Python3 提交中击败了
63.80%
的用户
通过测试用例：
49 / 49
"""
