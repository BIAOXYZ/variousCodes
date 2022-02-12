class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        # 今天第一次用，效果还可以吧。感觉以后就用这种全 tuple 的形式吧。
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def is_legal_coor(coor):
            x, y = coor[0], coor[1]
            return 0 <= x < m and 0 <= y < n
        def is_outside_coor(coor):
            # 用一下列表拆包
            x, y = coor
            return x in [0, m-1] or y in [0, n-1]
        
        totalOnes = 0
        outsideConnectedOnes = 0
        visited = set()
        def dfs(coor):
            # 在 dfs 开头处理是否遍历过的逻辑比较好，否则不但在下面的for循环
            # 处也去检测一下，后面最外层主程序的for循环也得处理。
            if coor in visited or grid[coor[0]][coor[1]] == 0:
                return
            else:
                nonlocal outsideConnectedOnes
                outsideConnectedOnes += 1
                visited.add(coor)
            x, y = coor
            nextCoors = [(x+d[0], y+d[1]) for d in directions]
            for nextCoor in nextCoors:
                if is_legal_coor(nextCoor):
                    dfs(nextCoor)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    totalOnes += 1
                    if is_outside_coor((i,j)):
                        dfs((i,j))
        return totalOnes - outsideConnectedOnes
        
"""
https://leetcode-cn.com/submissions/detail/267416669/

执行用时：208 ms, 在所有 Python3 提交中击败了31.18%的用户
内存消耗：18.4 MB, 在所有 Python3 提交中击败了5.09%的用户
通过测试用例：
57 / 57
"""
