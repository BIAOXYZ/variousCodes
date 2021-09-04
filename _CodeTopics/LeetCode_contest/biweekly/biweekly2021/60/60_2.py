class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m, n = len(land), len(land[0])
        visited = set()
        res = []
        
        def find_downright_coordinate(row, col):
            rowBreakFlag, colBreakFlag = False, False
            for i in range(row+1, m):
                if land[i][col] == 0:
                    rowBreakFlag = True
                    break
            for j in range(col+1, n):
                if land[row][j] == 0:
                    colBreakFlag = True
                    break
            rightRow = m - 1 if not rowBreakFlag else i - 1
            downCol = n - 1 if not colBreakFlag else j - 1
            res.append([row, col, rightRow, downCol])
            for i in range(row, rightRow+1):
                for j in range(col, downCol+1):
                    visited.add((i, j))
        
        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                else:
                    if land[i][j] == 1:
                        find_downright_coordinate(i, j)       
        return res
    
"""
https://leetcode-cn.com/submissions/detail/215222166/

217 / 217 个通过测试用例
状态：通过
执行用时: 448 ms
内存消耗: 44.3 MB
"""
