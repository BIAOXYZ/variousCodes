class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        n = len(matrix)
        base = range(1, n+1)
        for row in matrix:
            if sorted(row) != base:
                return False
        cols = [[matrix[i][j] for i in range(n)] for j in range(n)]
        for col in cols:
            if sorted(col) != base:
                return False
        return True
    
"""
https://leetcode-cn.com/submissions/detail/256473961/

214 / 214 个通过测试用例
状态：通过
执行用时: 84 ms
内存消耗: 13.7 MB
"""
