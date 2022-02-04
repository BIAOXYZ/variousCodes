class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def is_legal_coor(coor):
            x, y = coor[0], coor[1]
            return 0 <= x < m and 0 <= y < n
        
        res = 0
        def backtrack(coor, visited, currSum):
            nextCoors = [[coor[0]+d[0], coor[1]+d[1]] for d in directions]
            nextLegalCoors = list(filter(is_legal_coor, nextCoors))
            for nextx, nexty in nextLegalCoors:
                if grid[nextx][nexty] == 0 or (nextx, nexty) in visited:
                    continue
                currSum += grid[nextx][nexty]
                visited.add((nextx, nexty))
                backtrack([nextx, nexty], visited, currSum)
                visited.remove((nextx, nexty))
                currSum -= grid[nextx][nexty]
            nonlocal res
            res = max(res, currSum)
        
        for i in range(m):
            for j in range(n):
                # 发现真正的问题了：确实没必要从 0 的格子开始！
                # 而且换个角度想想：如果某个最大值路线是从 0 开始得到的，
                ## 那么肯定从这个 0 的周围的几个非 0 的位置开始也能得到。
                # 所以问题出在了开始时没有加上起始节点的黄金数量。。。也就是
                ## 不应该是： backtrack([i,j], set(), 0)
                if grid[i][j] > 0:
                    # 直接用 visited = set((i,j)) 不行，应该是会干扰，服了。。。
                    visited = set()
                    visited.add((i,j))
                    backtrack([i,j], visited, grid[i][j])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/264824182/

执行用时：1980 ms, 在所有 Python3 提交中击败了5.45%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了23.76%的用户
通过测试用例：
51 / 51
"""
