class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def is_legal_coordinate(x, y):
            if x < 0 or x > rows - 1: return False
            if y < 0 or y > cols - 1: return False
            return True
        
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        res = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    continue 
                neighbors = [[x-1,y], [x+1,y], [x,y-1], [x,y+1]]
                tmp = 0
                for neighbor in neighbors:
                    if not is_legal_coordinate(neighbor[0], neighbor[1]) or grid[neighbor[0]][neighbor[1]] == 0:
                        tmp += 1
                res += tmp
        return res
        
"""
https://leetcode-cn.com/submissions/detail/119649482/

5833 / 5833 个通过测试用例
状态：通过
执行用时: 276 ms
内存消耗: 13.1 MB

执行用时：276 ms, 在所有 Python 提交中击败了70.73%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了37.84%的用户
"""
