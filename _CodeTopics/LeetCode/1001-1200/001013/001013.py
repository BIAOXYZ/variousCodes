class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        summation = sum(A)
        if summation % 3 != 0:
            return False
        summation, length = summation / 3, len(A)
        
        currSum = A[0]
        ind1 = 1
        while ind1 <= length - 1 and currSum != summation:
            currSum += A[ind1]; ind1 += 1
        if currSum == summation:
            currSum = A[ind1]
            ind2 = ind1 + 1
            while ind2 <= length - 1 and currSum != summation:
                currSum += A[ind2]; ind2 += 1
            if currSum == summation and ind2 <= length - 1:
                return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/123677370/

55 / 55 个通过测试用例
状态：通过
执行用时: 48 ms
内存消耗: 16.6 MB

执行用时：48 ms, 在所有 Python 提交中击败了61.95%的用户
内存消耗：16.6 MB, 在所有 Python 提交中击败了27.78%的用户
"""
