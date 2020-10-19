class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        def getOuterElem(mtx, res):
            # h代表height, 也就是矩阵的行数；w代表width，也就是矩阵的列数。
            h = len(mtx)
            ###print "h is: ",h
            ###print "mtx is: ", mtx
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
        print 12345
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
执行结果：通过 显示详情
执行用时 :4 ms, 在所有 Python 提交中击败了100.00% 的用户
内存消耗 :12.7 MB, 在所有 Python 提交中击败了7.69%的用户
炫耀一下:
"""
"""
# https://leetcode-cn.com/submissions/detail/76611916/

22 / 22 个通过测试用例
	状态：通过
执行用时：4 ms
内存消耗：12.7 MB
"""
"""
本来还挺高兴的，但是后面同样的代码到跟这个一模一样的题目去提交时有用例没过，一下子高兴不起来了。。。

面试题29. 顺时针打印矩阵 https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/submissions/
"""
