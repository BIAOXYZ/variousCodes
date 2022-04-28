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
        move = move_p + move_a
        visited_p, visited_a = reachPacific.copy(), reachAtlantic.copy()
        def dfs_pacific(x, y):
            coor = (x, y)
            if coor in visited_p:
                return coor in reachPacific
            visited_p.add(coor)
            tmpRes = False
            for dx, dy in move:
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
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if (not is_legal_coordinate(nx, ny)) or (heights[nx][ny] > heights[x][y]):
                    continue 
                tmpRes = tmpRes or dfs_atlantic(nx, ny)
                if tmpRes:
                    break
            if tmpRes:
                reachAtlantic.add(coor)
            return tmpRes

        for i in range(m):
            for j in range(n):
                dfs_pacific(i, j)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dfs_atlantic(i, j)
        return sorted([list(elem) for elem in reachPacific & reachAtlantic])
        
"""
https://leetcode-cn.com/submissions/detail/306860482/

85 / 113 个通过测试用例
状态：解答错误

输入：
[[12,7,7,14,6,17,12,17,8,18,9,5],[6,8,12,5,3,6,2,14,19,6,18,13],[0,6,3,8,8,10,8,17,13,13,13,12],[5,6,8,8,15,16,19,14,7,11,2,3],[7,18,2,7,10,10,3,14,13,15,15,7],[18,6,19,4,12,3,3,2,6,6,19,6],[3,18,5,16,19,6,3,12,6,0,14,11],[9,10,17,12,10,11,11,9,0,0,12,0],[4,13,3,0,4,12,9,5,6,17,10,11],[18,3,5,0,8,19,18,4,8,19,1,3],[16,2,14,6,4,14,7,2,9,7,13,18],[0,16,19,16,16,4,15,19,7,0,3,16],[13,8,12,8,2,3,5,18,6,15,18,6],[4,10,8,1,16,0,6,0,14,10,11,8],[7,1,3,4,11,12,9,0,6,2,17,5],[1,16,6,1,0,19,11,1,5,7,8,2],[4,1,14,13,14,7,3,7,1,9,15,18],[14,11,6,14,14,14,4,0,11,17,1,9],[3,14,2,10,3,1,9,16,1,13,0,15],[8,9,13,5,5,7,10,1,4,5,0,9],[13,16,15,5,17,6,16,13,5,7,3,15],[5,1,12,19,3,13,0,0,3,10,6,13],[12,17,9,16,16,6,2,6,12,15,14,16],[7,7,0,6,4,15,1,7,17,5,2,12],[3,17,0,2,4,5,11,7,16,16,16,13],[3,7,16,11,2,16,14,9,16,17,10,3],[12,18,17,17,5,15,1,2,12,12,5,7],[11,10,10,0,11,7,17,14,5,15,2,16],[7,19,14,7,6,2,4,16,11,19,14,14],[6,17,6,6,6,15,9,12,8,13,1,7],[16,3,15,0,18,17,0,11,3,16,11,12],[15,12,4,6,19,15,17,7,3,9,2,11]]
输出：
[[0,9],[0,10],[0,11],[1,10],[1,11],[30,0],[31,0]]
预期结果：
[[0,9],[0,10],[0,11],[1,8],[1,10],[1,11],[30,0],[31,0]]
"""
