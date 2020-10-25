class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        length = len(A)
        maxMountainLen = 0
        left = 0

        while left <= length - 3:
            right = left + 1
            originalLeft = left
            while left <= length - 3 and A[left] < A[left+1]:
                left += 1
                if A[left] == A[left+1]:
                    right = left + 1
                    break
                elif A[left] > A[left+1]:
                    right = left + 1
                    while right <= length - 1 and A[right] > A[right+1]:
                        right += 1
                    # 这里需要减去的是originalLeft，因为在寻找山峰左半边的时候left一直在变。
                    maxMountainLen = max(maxMountainLen, right - originalLeft + 1)
            left = right
        return maxMountainLen
        
"""
https://leetcode-cn.com/submissions/detail/118563783/

7 / 72 个通过测试用例
状态：执行出错

执行出错信息：
Line 22: IndexError: list index out of range
最后执行的输入：
[0,1,2,3,4,5,4,3,2,1,0]
"""
