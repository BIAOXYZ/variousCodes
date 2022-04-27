class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m, n = len(heights), len(heights[0])
        reachPacific = set()
        reachAtlantic = set()
        for i in range(m):
            reachPacific.add((i, 0))
            reachAtlantic.add((i, n-1))
        for j in range(n):
            reachPacific.add((0, j))
            reachAtlantic.add((m-1, j))
        
        def is_legal_coordinate(x, y):
            return 0 <= x < m and 0 <= y < n

        move_p, move_a = [(0,-1),(-1,0)], [(0,1),(1,0)]
        visited_p, visited_a = reachPacific.copy(), reachAtlantic.copy()
        def dfs_pacific(x, y):
            coor = (x, y)
            if coor in visited_p:
                return coor in reachPacific
            visited_p.add(coor)
            tmpRes = False
            for dx, dy in move_p:
                nx, ny = x + dx, y + dy
                if (not is_legal_coordinate(nx, ny)) or (heights[nx][ny] > heights[x][y]):
                    continue 
                tmpRes = tmpRes or dfs_pacific(nx, ny)
                if tmpRes:
                    break
            if tmpRes:
                reachPacific.add(coor)
            return tmpRes
        def dfs_atlantic(x, y):
            coor = (x, y)
            if coor in visited_a:
                return coor in reachAtlantic
            visited_a.add(coor)
            tmpRes = False
            for dx, dy in move_a:
                nx, ny = x + dx, y + dy
                if (not is_legal_coordinate(nx, ny)) or (heights[nx][ny] > heights[x][y]):
                    continue 
                tmpRes = tmpRes or dfs_atlantic(nx, ny)
                if tmpRes:
                    break
            if tmpRes:
                reachAtlantic.add(coor)

        for i in range(1, m):
            for j in range(1, n):
                dfs_pacific(i, j)
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dfs_atlantic(i, j)
        return sorted([list(elem) for elem in reachPacific & reachAtlantic])
        
"""
https://leetcode-cn.com/submissions/detail/306404956/

50 / 113 个通过测试用例
状态：解答错误

输入：
[[1,2,3],[8,9,4],[7,6,5]]
输出：
[[0,2],[1,0],[1,1],[1,2],[2,0],[2,2]]
预期结果：
[[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
"""
