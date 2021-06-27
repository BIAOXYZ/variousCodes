class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        def loop_rotate(row1, col1, row2, col2, grid):
            first = grid[row1][col1]
            for j in range(col1, col2):
                grid[row1][j] = grid[row1][j+1]
            for i in range(row1, row2):
                grid[i][col2] = grid[i+1][col2]
            for j in range(col2, col1, -1):
                grid[row2][j] = grid[row2][j-1]
            for i in range(row2, row1+1, -1):
                grid[i][col1] = grid[i-1][col1]
            grid[row1+1][col1] = first
        
        m, n = len(grid), len(grid[0])
        row1, row2, col1, col2 = 0, m-1, 0, n-1
        while row1 < row2 and col1 < col2:
            modnum = 2 * (row2-row1+1) + 2 * (col2 - 1 - col1)
            newk = k % modnum
            for i in range(newk):
                loop_rotate(row1, col1, row2, col2, grid)
            row1 += 1; col1 += 1; row2 -= 1; col2 -= 1
        return grid
    
"""
https://leetcode-cn.com/submissions/detail/190078359/

68 / 68 个通过测试用例
状态：通过
执行用时: 220 ms
内存消耗: 13.5 MB
"""
