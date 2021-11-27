class Solution(object):
    def countPyramids(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        def is_legal(x, y):
            return 0 <= x < m and 0 <= y < n
        
        res = [0]
        def dfs(coor):
            x, y = coor[0], coor[1]
            incr = 1
            nextx, nexty1, nexty2 = x + incr, y - incr, y + incr
            while is_legal(nextx, nexty1) and is_legal(nextx, nexty2):
                if all(grid[nextx][col] == 1 for col in range(nexty1, nexty2 + 1)):
                    res[0] += 1
                    incr += 1
                    nextx, nexty1, nexty2 = x + incr, y - incr, y + incr
                else:
                    break
            decr = 1
            nextx, nexty1, nexty2 = x - decr, y - decr, y + decr
            while is_legal(nextx, nexty1) and is_legal(nextx, nexty2):
                if all(grid[nextx][col] == 1 for col in range(nexty1, nexty2 + 1)):
                    res[0] += 1
                    decr += 1
                    nextx, nexty1, nexty2 = x - decr, y - decr, y + decr
                else:
                    break
        
        for i in range(m):
            for j in range(1, n-1):
                dfs([i, j])
        return res[0]
    
"""
https://leetcode-cn.com/submissions/detail/242950842/

20 / 49 个通过测试用例
状态：解答错误

输入：
[[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]
输出：
16
预期：
13
"""
