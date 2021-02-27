class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        length = len(A)
        if length == 1:
            return True
        
        sign = set([])
        for i in range(1, length):
            if A[i] != A[i-1]:
                sign.add(abs(A[i]-A[i-1]) / (A[i]-A[i-1]))
                if len(sign) > 1:
                    return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/149305436/

366 / 366 个通过测试用例
状态：通过
执行用时: 416 ms
内存消耗: 18 MB

执行用时：416 ms, 在所有 Python 提交中击败了95.19%的用户
内存消耗：18 MB, 在所有 Python 提交中击败了46.15%的用户
"""
