class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        length = len(A)
        dpleft = [0 for i in range(length)]
        dpright = [0] * length
        maxMountainLen = 0

        for i in range(1, length-1):
            if A[i] > A[i-1]:
                dpleft[i] = dpleft[i-1] + 1
            else:
                dpleft[i] = 0
        for i in range(length-2, 0, -1):
            if A[i] > A[i+1]:
                dpright[i] = dpright[i+1] + 1
            else:
                dpright[i] = 0

        for i in range(1, length-1):
            if dpleft[i] > 0 and dpright[i] > 0:
                tmp = dpleft[i] + dpright[i] + 1
                maxMountainLen = max(maxMountainLen, tmp)
        return maxMountainLen
        
"""
https://leetcode-cn.com/submissions/detail/118487229/

72 / 72 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 14 MB

执行用时：52 ms, 在所有 Python 提交中击败了71.43%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了9.09%的用户
"""
