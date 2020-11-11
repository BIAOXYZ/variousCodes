class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        length = len(A)
        for i in range(length):
            if i % 2 != A[i] % 2:
                for j in range(i+1,length,2):
                    if j % 2 != A[j] % 2:
                        A[i], A[j] = A[j], A[i]
        return A
        
"""
https://leetcode-cn.com/submissions/detail/122781367/

59 / 61 个通过测试用例
状态：超出时间限制
"""
