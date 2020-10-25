class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        length = len(A)
        maxMountainLen = 0

        for i in range(1, length-1):
            tmp = 0
            left, flagleft = i - 1, False
            while left >= 0:
                if A[left] < A[left+1]:
                    flagleft = True
                    tmp += 1
                    left -= 1
                else:
                    break
            right, flagright = i + 1, False
            while right <= length - 1:
                if A[right] < A[right-1]:
                    flagright = True
                    tmp += 1
                    right += 1
                else:
                    break
            # 按题目要求，山峰不能只有半边。。。        
            if flagleft and flagright:
                tmp += 1
                maxMountainLen = max(tmp, maxMountainLen)
        return maxMountainLen
        
"""
https://leetcode-cn.com/submissions/detail/118474676/

15 / 72 个通过测试用例
状态：超出时间限制
"""
