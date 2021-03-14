class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # 这个是 `000054.py` 的去注释版本，除了注释以外两个是完全一样的。
        # 当时这个还不是每日一题。结果今天（2021.03.15）成了每日一题。

        def getOuterElem(mtx, res):
            h = len(mtx)
            w = len(mtx[0])
            if h == 1:
                for i in range(w):
                    res.append(mtx[0][i])
                return res
            if w == 1:
                for i in range(h):
                    res.append(mtx[i][0])
                return res
            for i in range(w):
                res.append(mtx[0][i])
            for i in range(1,h):
                res.append(mtx[i][w-1])
            for i in range(w-2,-1,-1):
                res.append(mtx[h-1][i])
            for i in range(h-2,0,-1):
                if i == 0:
                    break
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
        if h == 0 or w == 0:
            return res
        else:
            getOuterElem(matrix, res)
            return res
        
"""
https://leetcode-cn.com/submissions/detail/155226006/

22 / 22 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.1 MB

执行用时：12 ms, 在所有 Python 提交中击败了91.27%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了27.40%的用户
"""
