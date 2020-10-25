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
                    # 因为后面还有个A[right+1]，所以这里right到不了length-1，最多到length-2。
                    while right <= length - 2 and A[right] > A[right+1]:
                        right += 1
                    # 这里需要减去的是originalLeft，因为在寻找山峰左半边的时候left一直在变。
                    maxMountainLen = max(maxMountainLen, right - originalLeft + 1)
            left = right
        return maxMountainLen
        
"""
https://leetcode-cn.com/submissions/detail/118566994/

72 / 72 个通过测试用例
状态：通过
执行用时: 7024 ms
内存消耗: 13.8 MB

执行用时：7024 ms, 在所有 Python 提交中击败了7.14%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了12.12%的用户
"""
"""
双指针这个怎么这么慢，提交完跑的时候，我都以为这个要超时了。。。
"""
