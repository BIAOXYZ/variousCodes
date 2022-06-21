class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # 并查集写法
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(grid), len(grid[0])
        def is_legal_coordinate(x, y):
            return 0 <= x < m and 0 <= y < n

        # 先使用无路径压缩的 find，和无按秩合并的 union。
        # def find(x):
        #     if fa[x] != x:
        #         return find(fa[x])
        #     return fa[x]
        # def union(x, y):
        #     fa[fa[y]] = fa[x]

        # 我擦，不知道为啥普通版的两个并查集函数有个用例过不去，换了下面带
        # 路径压缩和按秩合并的加强版后，那个用例能过。现在也没法单步，服了。。。
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            # TODO: 只能说大概是这句错了，因为每次求 fax, fay 的时候最好再算一次
            # 最新的，而不是用 fa 里已有的结果。但是错误用例太复杂了，一时分析不出来。
            # fax, fay = fa[x], fa[y]
            fax, fay = find(x), find(y)
            if fax != fay:
                if fax > fay:
                    fax, fay = fay, fax
                fa[fay] = fax
        
        # 这里没必要用二维数组，而且可能还没有压成一维方便。
        # fa = [[-1 for _ in range(n)] for _ in range(m)]
        fa = [-1 for _ in range(m*n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    compoundInd = i * n + j
                    fa[compoundInd] = compoundInd
        ## print(fa)
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if is_legal_coordinate(nx, ny) and grid[nx][ny] == '1':
                            compoundInd1, compoundInd2 = x * n + y, nx * n + ny
                            union(compoundInd1, compoundInd2)
        # print(fa)
        # for i in range(m):
        #     for j in range(n):
        #         if fa[i * n + j] == i * n + j:
        #             print((i,j), grid[i][j], i*n+j, fa[i*n+j])
        return sum(1 for i in range(m) for j in range(n) if fa[i * n + j] == i * n + j)
        
"""
https://leetcode.cn/submissions/detail/327814174/

执行用时：
200 ms
, 在所有 Python3 提交中击败了
6.95%
的用户
内存消耗：
27.4 MB
, 在所有 Python3 提交中击败了
6.76%
的用户
通过测试用例：
49 / 49
"""
