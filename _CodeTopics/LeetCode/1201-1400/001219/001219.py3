class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        # 打算先沿用 Python2 的 res[0] 写法，后面再改成 Python3 的 nonlocal。

        m, n = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def is_legal_coor(coor):
            x, y = coor[0], coor[1]
            return 0 <= x < m and 0 <= y < n
        
        res = [0]
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
            # 这还是比较少的（可能是第一次？）结束回溯状态在for循环往下回溯之前的写法。
            # 其实开始也还是一上来就在开头写的，但是后来发现这道题写这里更好。
            res[0] = max(res[0], currSum)
        
        for i in range(m):
            for j in range(n):
                # 上一个错的原因在这：虽然中间不能进入 0 的格子，但是初始状态可以从 0 的格子出发。。。
                backtrack([i,j], set(), 0)
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/264822463/

执行用时：6364 ms, 在所有 Python3 提交中击败了5.45%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了35.15%的用户
通过测试用例：
51 / 51
"""
