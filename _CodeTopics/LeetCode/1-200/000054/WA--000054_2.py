class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        def getOuterElem(mtx, res):
            # h代表height, 也就是矩阵的行数；w代表width，也就是矩阵的列数。
            h = len(mtx)
            w = len(mtx[0])
            if h == 1:
                for i in range(w):
                    res.append(mtx[0][i])
                ##print res
                return res
            if w == 1:
                for i in range(h):
                    res.append(mtx[i][0])
                ##print res
                return res
            for i in range(w):
                ##print mtx[0][i]
                res.append(mtx[0][i])
            for i in range(1,h):
                ##print mtx[i][w-1]
                res.append(mtx[i][w-1])
            for i in range(w-2,-1,-1):
                ##print mtx[h-1][i]
                res.append(mtx[h-1][i])
            for i in range(h-2,0,-1):
                if i == 0:
                    break
                ##print mtx[i][0]
                res.append(mtx[i][0])
        
        def getInnerMatrix(mtx):
            mtx.remove(mtx[0])
            mtx.remove(mtx[-1])
            for row in mtx:
                row.remove(row[0])
                row.remove(row[-1])

        if matrix == []:
            return []
        res = []
        h = len(matrix)
        w = len(matrix[0])
        while h > 1 and w > 1:
            getOuterElem(matrix, res)
            getInnerMatrix(matrix)
            h -= 2
            w -= 2
        if h == 0 and w == 0:
            return res
        else:
            getOuterElem(matrix, res)
            return res

"""
# https://leetcode-cn.com/submissions/detail/76610604/

10 / 22 个通过测试用例
	状态：执行出错
执行出错信息： Line 11: IndexError: list index out of range
最后执行的输入： [[2,5,8],[4,0,-1]]
"""
"""
这个判断应该是 or 而不是 and。否则一个2*3的矩阵本来一轮就完了，结果还要进去迭代一轮，于是就会index超出范围了。
if h == 0 or w == 0:
"""
