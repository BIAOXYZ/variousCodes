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
        
        currSum = 0
        ind1 = 0
        while ind1 <= length - 1 and currSum != summation:
            currSum += A[ind1]; ind1 += 1
        if currSum == summation:
            ind2 = ind1
            currSum = 0
            while ind2 <= length - 1 and currSum != summation:
                currSum += A[ind2]; ind2 += 1
            if currSum == summation:
                return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/123666251/

54 / 55 个通过测试用例
状态：解答错误

输入：
[1,-1,1,-1]
输出：
true
预期：
false
"""
