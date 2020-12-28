class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        # 矩阵的行数
        m = len(matrix)
        # 矩阵的列数
        n = len(matrix[0])
        lucknumberlist = []
        
        #for k in range(n):
        #    mat[k].ap
        
        for i in range(m):
            curr_row = matrix[i] 
            curr_row_min = min(curr_row)
            ind = curr_row.index(curr_row_min)
            for j in range(m):
                flag = 1
                if curr_row_min < matrix[j][ind]:
                    flag = 0
                    break
            if flag == 1:
                lucknumberlist.append(curr_row_min)
        return lucknumberlist
