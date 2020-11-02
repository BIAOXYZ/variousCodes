class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        length = len(A)
        if length < 3:
            return False
        if A[1] <= A[0]:
            return False

        flag = 1
        for i in range(2,length):
            if A[i] == A[i-1]:
                return False
            if flag == 1:
                if A[i] < A[i-1]:
                    flag = -1
            else:
                if A[i] > A[i-1]:
                    return False
        
        if flag == 1:
            return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/120534017/

51 / 51 个通过测试用例
状态：通过
执行用时: 180 ms
内存消耗: 14.6 MB

执行用时：180 ms, 在所有 Python 提交中击败了92.17%的用户
内存消耗：14.6 MB, 在所有 Python 提交中击败了5.56%的用户
"""
