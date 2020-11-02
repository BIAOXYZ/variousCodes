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
        return True
        
"""
https://leetcode-cn.com/submissions/detail/120533679/

50 / 51 个通过测试用例
状态：解答错误

输入：
[0,1,2,3,4,5,6,7,8,9]
输出：
true
预期：
false
"""
