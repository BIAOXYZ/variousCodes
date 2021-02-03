class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        n = len(nums)
        globalMax = currMax = sum(nums[:k])

        for i in range(k, n):
            if nums[i] > nums[i-k]:
                currMax += nums[i] - nums[i-k]
                globalMax = max(globalMax, currMax)
            else:
                currMax += nums[i] - nums[i-k]
        return globalMax * 1.0 / k
        
"""
https://leetcode-cn.com/submissions/detail/143531010/

123 / 123 个通过测试用例
状态：通过
执行用时: 744 ms
内存消耗: 15.9 MB

执行用时：744 ms, 在所有 Python 提交中击败了81.95%的用户
内存消耗：15.9 MB, 在所有 Python 提交中击败了35.34%的用户
"""
