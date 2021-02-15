class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        res = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                res += nums[i]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/145970465/

83 / 83 个通过测试用例
状态：通过
执行用时: 76 ms
内存消耗: 14.6 MB

执行用时：76 ms, 在所有 Python 提交中击败了30.10%的用户
内存消耗：14.6 MB, 在所有 Python 提交中击败了14.29%的用户
"""
