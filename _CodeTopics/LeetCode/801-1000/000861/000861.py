class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        def row_flip(lis):
            for i in range(len(lis)):
                lis[i] = 1 - lis[i]
        def calculate_binary_form(lis):
            res = 0
            multipler = 1
            for i in range(len(lis)-1, -1, -1):
                res += lis[i] * multipler
                multipler = multipler * 2
            return res
        
        for lis in A:
            if lis[0] == 0:
                row_flip(lis)
        
        rows, cols = len(A), len(A[0])
        for y in range(1, cols):
            numOfZero = 0
            for x in range(rows):
                if A[x][y] == 0:
                    numOfZero += 1
            if numOfZero > rows - numOfZero:
                for x in range(rows):
                    A[x][y] = 1 - A[x][y]
        
        res = 0
        for lis in A:
            res += calculate_binary_form(lis)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/129121431/

80 / 80 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 12.9 MB

执行用时：32 ms, 在所有 Python 提交中击败了34.78%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了50.00%的用户
"""
