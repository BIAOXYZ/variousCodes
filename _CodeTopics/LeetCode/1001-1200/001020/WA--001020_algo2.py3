from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def is_legal_coor(coor):
            x, y = coor[0], coor[1]
            return 0 <= x < m and 0 <= y < n
        def is_outside_coor(coor):
            # （在 BFS 里也）用一下列表拆包- -
            x, y = coor
            return x in [0, m-1] or y in [0, n-1]
        
        totalOnes = 0
        outsideConnectedOnes = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    totalOnes += 1
                    if is_outside_coor((i,j)) and (i,j) not in visited:
                        # 注意这里不能用 q = deque((i,j))，不然相当于是把整个 tuple (i,j) 里
                        # 的两个元素做成一个 deque，而不是 (i, j) 整体当成一个元素。
                        # 此外，本地试了下有： deque((i,j)) == deque([i,j])
                        q = deque([(i,j)])
                        while q:
                            for _ in range(len(q)):
                                coor = q.popleft()
                                visited.add(coor)
                                outsideConnectedOnes += 1
                                x, y = coor
                                nextCoors = [(x+d[0], y+d[1]) for d in directions]
                                for nextCoor in nextCoors:
                                    nextx, nexty = nextCoor
                                    # 加上上面那次，某个坐标是否在 visited 中需要在两处写判断的代码。如果像前一个dfs里
                                    # 那样放在 dfs 的逻辑中，应该也可以只需要在一处写判断，等会可以试试。
                                    if is_legal_coor(nextCoor) and grid[nextx][nexty] == 1 and nextCoor not in visited:
                                        q.append(nextCoor)
        return totalOnes - outsideConnectedOnes
        
"""
https://leetcode-cn.com/submissions/detail/267575733/

3 / 57 个通过测试用例
状态：解答错误

通过测试用例：
3 / 57
输入：
[[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]
输出：
-40
预期结果：
3
"""
