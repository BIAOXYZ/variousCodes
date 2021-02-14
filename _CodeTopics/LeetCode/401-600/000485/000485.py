class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        flag = False
        maxLen = currLen = 0
        for num in nums:
            if num == 1:
                if not flag:
                    flag = True
                    currLen = 1
                else:
                    currLen += 1
            else:
                if flag:
                    flag = False
                    maxLen = max(maxLen, currLen)
                    currLen = 0
        maxLen = max(maxLen, currLen)
        return maxLen
        
"""
https://leetcode-cn.com/submissions/detail/145771080/

41 / 41 个通过测试用例
状态：通过
执行用时: 296 ms
内存消耗: 13.2 MB

执行用时：296 ms, 在所有 Python 提交中击败了98.62%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了91.20%的用户
"""
