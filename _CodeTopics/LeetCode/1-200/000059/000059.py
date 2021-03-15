class Solution(object):
    
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        mtx = [[-1 for i in range(n)] for j in range(n)]
        
        def fill_outer(startInd, endInd, currNum):
            if startInd + 1 == endInd:
                mtx[startInd][startInd] = currNum
                return
            if startInd + 2 == endInd:
                mtx[startInd][startInd] = currNum; currNum += 1
                mtx[startInd][endInd-1] = currNum; currNum += 1
                mtx[endInd-1][endInd-1] = currNum; currNum += 1
                mtx[endInd-1][startInd] = currNum; currNum += 1
                return
            for i in range(startInd, endInd):
                mtx[startInd][i] = currNum; currNum += 1
            for j in range(startInd+1, endInd):
                mtx[j][endInd-1] = currNum; currNum += 1
            for i in range(endInd-2, startInd-1, -1):
                mtx[endInd-1][i] = currNum; currNum += 1
            for j in range(endInd-2, startInd, -1):
                mtx[j][startInd] = currNum; currNum += 1
        
        startInd, endInd = 0, n
        currNum = 1
        while endInd > startInd:
            fill_outer(startInd, endInd, currNum)
            currNum += 4*(endInd-startInd-1)
            startInd += 1
            endInd -= 1
        return mtx
        
"""
https://leetcode-cn.com/submissions/detail/155666874/

20 / 20 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.8 MB

执行用时：16 ms, 在所有 Python 提交中击败了78.25%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了92.29%的用户
"""
