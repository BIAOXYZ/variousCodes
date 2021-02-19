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
                currReverseNum += 1
                diffArr[i+K] -= 1    
                A[i] ^= currReverseNum
        for j in range(length-K+1, length):
            currReverseNum += diffArr[j]
            A[j] ^= currReverseNum
        return total if 0 not in A else -1
        
"""
https://leetcode-cn.com/submissions/detail/146944415/

74 / 110 个通过测试用例
状态：解答错误

输入：
[0,0,0,1,0,1,1,0]
3
输出：
-1
预期：
3
"""
