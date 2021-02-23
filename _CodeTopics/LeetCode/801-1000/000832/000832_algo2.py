class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        # 原地算法

        length = len(A)
        for i in range(length):
            if length % 2 == 1:
                for j in range(length/2 + 1):
                    A[i][j], A[i][length-1-j] = 1 - A[i][length-1-j], 1 - A[i][j]
            else:
                for j in range(length/2):
                    A[i][j], A[i][length-1-j] = 1 - A[i][length-1-j], 1 - A[i][j]
        return A
        
"""
https://leetcode-cn.com/submissions/detail/148134095/

82 / 82 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 12.9 MB

执行用时：40 ms, 在所有 Python 提交中击败了45.55%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了87.90%的用户
"""
