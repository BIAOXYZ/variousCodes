class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # 并查集写法
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(grid), len(grid[0])
        def is_legal_coordinate(x, y):
            return 0 <= x < m and 0 <= y < n

        # 先使用无路径压缩的 find，和无按秩合并的 union。
        def find(x):
            if fa[x] != x:
                return find(fa[x])
            return fa[x]
        def union(x, y):
            fa[fa[y]] = fa[x]

        # def find(x):
        #     if fa[x] != x:
        #         fa[x] = find(fa[x])
        #     return fa[x]
        # def union(x, y):
        #     fax, fay = fa[x], fa[y]
        #     if fax != fay:
        #         if fax > fay:
        #             fax, fay = fay, fax
        #         fa[fay] = fax
        
        # 这里没必要用二维数组，而且可能还没有压成一维方便。
        # fa = [[-1 for _ in range(n)] for _ in range(m)]
        fa = [-1 for _ in range(m*n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    compoundInd = i * n + j
                    fa[compoundInd] = compoundInd
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if is_legal_coordinate(nx, ny) and grid[nx][ny] == '1':
                            compoundInd1, compoundInd2 = x * n + y, nx * n + ny
                            union(compoundInd1, compoundInd2)
        return sum(1 for i in range(m) for j in range(n) if fa[i * n + j] == i * n + j)
        
"""
https://leetcode.cn/submissions/detail/327469543/

36 / 49 个通过测试用例
状态：解答错误

输入：
[["1","1","1","1","1","0","1","1","1","1"],["1","0","1","0","1","1","1","1","1","1"],["0","1","1","1","0","1","1","1","1","1"],["1","1","0","1","1","0","0","0","0","1"],["1","0","1","0","1","0","0","1","0","1"],["1","0","0","1","1","1","0","1","0","0"],["0","0","1","0","0","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","1"],["1","1","1","1","1","1","1","1","0","1"],["1","0","1","1","1","1","1","1","1","0"]]
输出：
5
预期结果：
2
"""
