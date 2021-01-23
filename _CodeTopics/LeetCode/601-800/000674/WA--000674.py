class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        
        maxLen = 1
        currLen = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                currLen += 1
            else:
                maxLen = max(maxLen, currLen)
                currLen = 1
        return maxLen
        
"""
https://leetcode-cn.com/submissions/detail/140654995/

26 / 36 个通过测试用例
状态：解答错误

输入：
[1,3,5,7]
输出：
1
预期：
4
"""
