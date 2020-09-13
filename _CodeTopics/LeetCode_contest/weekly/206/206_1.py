class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        rows, cols = len(mat), len(mat[0])
        res = 0
        
        def sum_of_column(j):
            ret = 0
            for i in range(rows):
                ret += mat[i][j]
            return ret
        
        for i in range(rows):
            if sum(mat[i]) != 1:
                continue
            for j in range(cols):
                if mat[i][j] != 1:
                    continue
                if sum_of_column(j) == 1:
                    res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/107496893/

95 / 95 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 12.8 MB
"""
