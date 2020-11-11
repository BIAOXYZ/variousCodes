class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        # O(n^2)的原地算法会超时，换成O(n)的非原地算法。

        length = len(A)
        res = [0 for _ in range(length)]
        evenptr, oddptr = 0, 1

        for i in range(length):
            if A[i] % 2 == 0:
                res[evenptr] = A[i]
                evenptr += 2
            else:
                res[oddptr] = A[i]
                oddptr += 2
        return res
        
"""
https://leetcode-cn.com/submissions/detail/122782020/

61 / 61 个通过测试用例
状态：通过
执行用时: 180 ms
内存消耗: 15.2 MB

执行用时：180 ms, 在所有 Python 提交中击败了90.53%的用户
内存消耗：15.2 MB, 在所有 Python 提交中击败了6.12%的用户
"""
