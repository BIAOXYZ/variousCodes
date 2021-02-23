class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        length = len(A)
        B = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            for j in range(length):
                B[i][j] = 1 - A[i][length-1-j]
        return B
        
"""
https://leetcode-cn.com/submissions/detail/148133268/

82 / 82 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13 MB

执行用时：32 ms, 在所有 Python 提交中击败了84.29%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了69.47%的用户
"""
