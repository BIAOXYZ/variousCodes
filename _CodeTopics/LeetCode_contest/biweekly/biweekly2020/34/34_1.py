class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        n = len(mat)
        sum = 0
        for i in range(n):
            sum += mat[i][i]
            if i != n - 1 - i:
                sum += mat[i][n-1-i]
        return sum
    
"""
https://leetcode-cn.com/submissions/detail/105124481/

113 / 113 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 12.8 MB
"""
