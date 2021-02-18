class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        length = len(A)
        left = right = 0
        permitZero = K
        maxLen = currLen = 0

        while right < length:
            if A[right] == 0:
                permitZero -= 1
            if permitZero >= 0:
                right += 1
            elif permitZero < 0:
                currLen = right - left
                maxLen = max(maxLen, currLen)
                while A[left] != 0:
                    left += 1
                left += 1; permitZero += 1; right += 1
        currLen = right - left
        maxLen = max(maxLen, currLen)
        return maxLen
        
"""
https://leetcode-cn.com/submissions/detail/146647424/

48 / 48 个通过测试用例
状态：通过
执行用时: 516 ms
内存消耗: 13.5 MB

执行用时：516 ms, 在所有 Python 提交中击败了79.07%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了50.39%的用户
"""
