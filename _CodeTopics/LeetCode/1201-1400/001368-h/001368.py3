from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        # （双端队列实现的）0-1 BFS
        
        directions_dic = {1:(0,1), 2:(0,-1), 3:(1,0), 4:(-1,0)}
        directions_list = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(grid), len(grid[0])
        costs = [[-1 for _ in range(n)] for _ in range(m)]
        
        def is_legal_coordinate(x, y):
            return 0 <= x < m and 0 <= y < n

        dq = deque()
        # tuple 的三个元素分别表示当前的代价，横坐标，纵坐标。
        dq.append((0, 0, 0))
        while dq:
            cost, x, y = dq.popleft()
            if costs[x][y] == -1:
                costs[x][y] = cost
            else:
                continue
            for dx, dy in directions_list:
                nx, ny = x + dx, y + dy
                if is_legal_coordinate(nx, ny):
                    arrowValue = grid[x][y]
                    if directions_dic[arrowValue] == (dx, dy):
                        dq.appendleft((cost, nx, ny))
                    else:
                        dq.append((cost+1, nx, ny))
        return costs[m-1][n-1]
        
"""
https://leetcode.cn/submissions/detail/327073227/

执行用时：
244 ms
, 在所有 Python3 提交中击败了
56.38%
的用户
内存消耗：
17.4 MB
, 在所有 Python3 提交中击败了
22.15%
的用户
通过测试用例：
68 / 68
"""
