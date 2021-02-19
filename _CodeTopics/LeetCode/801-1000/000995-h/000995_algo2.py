class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        length = len(A)
        total = 0
        diffArr = [0 for _ in range(length+1)]
        currReverseNum = 0

        for i in range(length-K+1):
            currReverseNum += diffArr[i]
            if (A[i] + currReverseNum) % 2 == 0:
                total += 1
                diffArr[i+K] -= 1
                currReverseNum += 1
                A[i] ^= (currReverseNum % 2)
            else:
                A[i] ^= (currReverseNum % 2)
        for j in range(length-K+1, length):
            currReverseNum += diffArr[j]
            A[j] ^= (currReverseNum % 2)
        return total if 0 not in A else -1
        
"""
https://leetcode-cn.com/submissions/detail/146945188/

110 / 110 个通过测试用例
状态：通过
执行用时: 776 ms
内存消耗: 14.5 MB

执行用时：776 ms, 在所有 Python 提交中击败了31.96%的用户
内存消耗：14.5 MB, 在所有 Python 提交中击败了54.64%的用户
"""
