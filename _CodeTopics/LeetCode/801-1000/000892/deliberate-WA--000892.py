class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # 还是有输入不对，不过打算先提了，如果后面还会回看的话到时候也容易记忆更深刻。

        def is_legal_coordinate(i, j):
            if i < 0 or i > n - 1: return False
            if j < 0 or j > n - 1: return False
            return True
        def calculate_lateral_area(i, j):
            res = 0
            neighbors = [[i-1,j], [i+1,j], [i,j-1], [i,j+1]]
            legal_neighbors = []
            for neighbor in neighbors:
                x, y = neighbor[0], neighbor[1]
                if is_legal_coordinate(x, y):
                    legal_neighbors.append(neighbor) 
            if i in [0, n-1] and j in [0, n-1]:
                res += 2 * grid[i][j]
                res += (2 - len(legal_neighbors)) * grid[i][j]
                for x, y in legal_neighbors:
                    res += max(0, grid[i][j] - grid[x][y])
            elif (i in [0, n-1] and j not in [0, n-1]) or (i not in [0, n-1] and j in [0, n-1]):
                res += grid[i][j]
                res += (3 - len(legal_neighbors)) * grid[i][j]
                for x, y in legal_neighbors:
                    res += max(0, grid[i][j] - grid[x][y])
            else:
                res += (4 - len(legal_neighbors)) * grid[i][j]
                for x, y in legal_neighbors:
                    res += max(0, grid[i][j] - grid[x][y])
            return res                

        n = len(grid)
        res = 0
        for i in range(n):
            for j in range(n):
                res += calculate_lateral_area(i, j)
        return res + 2 * n * n
        
"""
https://leetcode-cn.com/submissions/detail/188061221/

24 / 90 个通过测试用例
状态：解答错误

最后执行的输入：
[[1,0],[0,2]]
输出：
20
预期结果：
16
"""
