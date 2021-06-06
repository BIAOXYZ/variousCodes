class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        
        n = len(mat)
        
        def mtx_equal(m1, m2):
            for i in range(n):
                for j in range(n):
                    if m1[i][j] != m2[i][j]:
                        return False
            return True
        
        if mtx_equal(mat, target):
            return True
        mat1 = [[2 for _ in range(n)] for _ in range(n)]
        mat2 = [[2 for _ in range(n)] for _ in range(n)]
        mat3 = [[2 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # 草TM的！申请mat1，mat2，mat3的时候用常用的列表推导式就没问题了，所以是 [[2]*n]*n 的问题！草！
                mat1[i][j] = mat[n-1-j][i]
        for i in range(n):
            for j in range(n):        
                mat2[i][j] = mat1[n-1-j][i]
        for i in range(n):
            for j in range(n):
                mat3[i][j] = mat2[n-1-j][i]
        return mtx_equal(mat1, target) or mtx_equal(mat2, target) or mtx_equal(mat3, target)
    
"""
https://leetcode-cn.com/submissions/detail/184387319/

109 / 109 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 12.8 MB
"""
