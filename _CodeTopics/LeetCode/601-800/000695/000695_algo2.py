class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # BFS

        def is_legal_coordinate_v2(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def bfs_and_count_one(coor):
            numOfOne = 0
            stk = [coor]
            while stk:
                currCoor = stk.pop(0)
                x, y = currCoor[0], currCoor[1]
                neighbors = [[x-1,y], [x+1,y], [x,y-1], [x,y+1]]
                for neighbor in neighbors:
                    newx, newy = neighbor[0], neighbor[1]
                    if is_legal_coordinate_v2(newx, newy) and grid[newx][newy] == 1 and [newx,newy] not in visited:
                        visited.append([newx,newy])
                        numOfOne += 1
                        stk.append([newx,newy])
            return numOfOne

        rows, cols = len(grid), len(grid[0])
        visited = []
        maxArea = currArea = 0

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and [x,y] not in visited:
                    visited.append([x,y])
                    currArea += 1
                    currArea += bfs_and_count_one([x,y])
                    maxArea = max(maxArea, currArea)
                    currArea = 0
        return maxArea
        
"""
https://leetcode-cn.com/submissions/detail/145933905/

726 / 726 个通过测试用例
状态：通过
执行用时: 956 ms
内存消耗: 13.4 MB

执行用时：956 ms, 在所有 Python 提交中击败了5.22%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了85.14%的用户
"""
