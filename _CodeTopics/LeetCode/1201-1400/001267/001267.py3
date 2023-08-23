class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dicRow, dicCol = {i:[] for i in range(m)}, {i:[] for i in range(n)}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    tup = (i, j)
                    dicRow[i].append(tup)
                    dicCol[j].append(tup)
        
        se = set()
        for dic in [dicRow, dicCol]:
            for v in dic.values():
                if len(v) > 1:
                    se.update(v)
        return len(se)
        
"""
https://leetcode.cn/problems/count-servers-that-communicate/submissions/459323256/

时间
详情
68ms
击败 89.86%使用 Python3 的用户
内存
详情
17.73MB
击败 60.87%使用 Python3 的用户
"""
