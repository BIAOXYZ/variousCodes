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
        def is_legal_coordinate_for_square(x, y):
            if x < 0 or x > length - 1: return False
            if y < 0 or y > length - 1: return False
            return True

        length = len(grid)
        rottenOrange, totalOrange = [], []
        res = 0
        for i in range(length):
            for j in range(length):
                if grid[i][j] == 1:
                    totalOrange.append([i,j])
                if grid[i][j] == 2:
                    totalOrange.append([i,j])
                    rottenOrange.append([i,j])
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
                    if is_legal_coordinate_for_square(newx, newy) and grid[newx][newy] == 1:
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
https://leetcode-cn.com/submissions/detail/115111762/

6 / 303 个通过测试用例
状态：解答错误

输入：
[[0,1]]
输出：
0
预期：
-1
"""
