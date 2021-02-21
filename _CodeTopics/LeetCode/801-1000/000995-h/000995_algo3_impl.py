class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        # 无差分数组思想的实现，但是是无异或版本——也就是精确计算翻转次数的具体数目。

        length = len(A)
        total = 0
        currReverseNum = 0

        for i in range(length):
            if i >= K and A[i-K] >= 2:
                currReverseNum -= 1
                A[i-K] -= 2
            if (A[i] + currReverseNum) % 2 == 0:
                if i + K > length:
                    return -1
                total += 1
                A[i] += 2
                currReverseNum += 1
        return total
        
"""
https://leetcode-cn.com/submissions/detail/147432420/

110 / 110 个通过测试用例
状态：通过
执行用时: 876 ms
内存消耗: 14.4 MB

执行用时：876 ms, 在所有 Python 提交中击败了16.03%的用户
内存消耗：14.4 MB, 在所有 Python 提交中击败了61.86%的用户
"""
