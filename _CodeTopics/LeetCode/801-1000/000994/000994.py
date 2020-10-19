class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def lists_are_equal(l1, l2):
            l1.sort()
            l2.sort()
            return True if l1 == l2 else False
        def is_legal_coordinate(x, y):
            if x < 0 or x > rows - 1: return False
            if y < 0 or y > cols - 1: return False
            return True

        rows, cols = len(grid), len(grid[0])
        rottenOrange, freshOrange, totalOrange = [], [], []
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    totalOrange.append([i,j])
                    freshOrange.append([i,j])
                if grid[i][j] == 2:
                    totalOrange.append([i,j])
                    rottenOrange.append([i,j])
        if not rottenOrange and freshOrange:
            return -1
        if lists_are_equal(totalOrange, rottenOrange):
            return res
        
        q = rottenOrange[:]
        while q:
            nextLevel = []
            for coor in q:
                x, y = coor[0], coor[1]
                neighbors = [[x-1,y], [x+1,y], [x,y-1], [x,y+1]]
                for neighbor in neighbors:
                    newx, newy = neighbor[0], neighbor[1]
                    if is_legal_coordinate(newx, newy) and grid[newx][newy] == 1:
                        grid[newx][newy] = 2
                        nextLevel.append(neighbor)
                        rottenOrange.append(neighbor)
            q = nextLevel[:]
            if nextLevel:
                res += 1
        
        if lists_are_equal(totalOrange, rottenOrange):
            return res
        else:
            return -1
"""
https://leetcode-cn.com/submissions/detail/115114392/

303 / 303 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 12.4 MB

执行用时：52 ms, 在所有 Python 提交中击败了17.77%的用户
内存消耗：12.4 MB, 在所有 Python 提交中击败了51.16%的用户
"""
