class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return -1

        totalSum = sum(nums)
        if totalSum - nums[0] == 0:
            return 0

        currSum = 0
        for i in range(1, len(nums)):
            currSum += nums[i-1]
            if currSum * 2 == totalSum - nums[i]:
                return i
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/141710962/

742 / 742 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 13.8 MB

执行用时：36 ms, 在所有 Python 提交中击败了79.80%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了55.90%的用户
"""
