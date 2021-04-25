class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if not A:
            return 0
        
        res = 0
        A.sort()
        for i in range(1, len(A)):
            if A[i] <= A[i-1]:
                res += A[i-1] - A[i] + 1
                A[i] = A[i-1] + 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/171886952/

59 / 59 个通过测试用例
状态：通过
执行用时: 296 ms
内存消耗: 17.4 MB

执行用时：296 ms, 在所有 Python 提交中击败了64.71%的用户
内存消耗：17.4 MB, 在所有 Python 提交中击败了61.76%的用户
"""
