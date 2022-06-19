import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        # （堆来实现，和双端队列实现很类似，大部分代码无需改动）0-1 BFS
        
        directions_dic = {1:(0,1), 2:(0,-1), 3:(1,0), 4:(-1,0)}
        directions_list = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(grid), len(grid[0])
        costs = [[-1 for _ in range(n)] for _ in range(m)]
        
        def is_legal_coordinate(x, y):
            return 0 <= x < m and 0 <= y < n
        
        hp = []
        heapq.heapify(hp)
        heapq.heappush(hp, (0, 0, 0))
        while hp:
            cost, x, y = heapq.heappop(hp)
            if costs[x][y] == -1:
                costs[x][y] = cost
            else:
                continue
            for dx, dy in directions_list:
                nx, ny = x + dx, y + dy
                if is_legal_coordinate(nx, ny):
                    arrowValue = grid[x][y]
                    if directions_dic[arrowValue] == (dx, dy):
                        heapq.heappush(hp, (cost, nx, ny))
                    else:
                        heapq.heappush(hp, (cost+1, nx, ny))
        return costs[m-1][n-1]
        
"""
https://leetcode.cn/submissions/detail/327078286/

执行用时：
376 ms
, 在所有 Python3 提交中击败了
14.77%
的用户
内存消耗：
17.5 MB
, 在所有 Python3 提交中击败了
22.15%
的用户
通过测试用例：
68 / 68
"""
