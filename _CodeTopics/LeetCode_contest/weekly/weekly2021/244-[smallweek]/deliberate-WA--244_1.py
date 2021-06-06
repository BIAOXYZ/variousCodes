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
        mat1, mat2, mat3 = [[2]*n]*n, [[2]*n]*n, [[2]*n]*n
        for i in range(n):
            for j in range(n):
                # 我TM裂开了。。。我单步跟了下不知道为什么这个操蛋的语句会一次改掉mat1里两个元素的值。。。
                mat1[i][j] = mat[n-1-j][i]
        for i in range(n):
            for j in range(n):        
                mat2[i][j] = mat1[n-1-j][i]
        for i in range(n):
            for j in range(n):
                mat3[i][j] = mat2[n-1-j][i]
        return mtx_equal(mat1, target) or mtx_equal(mat2, target) or mtx_equal(mat3, target)
    
"""
https://leetcode-cn.com/submissions/detail/184385430/

58 / 109 个通过测试用例
状态：解答错误

最后执行的输入：
[[0,1],[1,0]]
[[1,0],[0,1]]
"""
