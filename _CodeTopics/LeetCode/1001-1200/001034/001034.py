class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """

        m, n = len(grid), len(grid[0])
        
        def is_legal_coordinate(x, y):
            return 0 <= x < m and 0 <= y < n

        currColor = grid[row][col]
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visitedConnectedComponents = set()

        def dfs(x, y):
            if tuple([x, y]) in visitedConnectedComponents:
                return
            visitedConnectedComponents.add(tuple([x, y]))
            for move in moves:
                nextX, nextY = x + move[0], y + move[1]
                if is_legal_coordinate(nextX, nextY) and grid[nextX][nextY] == currColor:
                    dfs(nextX, nextY)
        
        dfs(row, col)
        ##print visitedConnectedComponents

        def is_boundary(x, y):
            return x == 0 or x == m - 1 or y == 0 or y == n - 1
        
        needChange = set()
        for x, y in visitedConnectedComponents:
            if is_boundary(x, y) or any(grid[x + move[0]][y + move[1]] != currColor for move in moves):
                needChange.add(tuple([x, y]))
        for x, y in needChange:
            grid[x][y] = color
        return grid
        
"""
https://leetcode-cn.com/submissions/detail/245981820/

执行用时：28 ms, 在所有 Python 提交中击败了37.50%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了12.50%的用户
通过测试用例：
154 / 154
"""
