class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return -1

        totalSum = sum(nums)
        currSum = 0
        for i in range(1, len(nums)):
            currSum += nums[i-1]
            if currSum * 2 == totalSum - nums[i]:
                return i
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/141710539/

589 / 742 个通过测试用例
状态：解答错误

输入：
[-1,-1,-1,0,1,1]
输出：
-1
预期：
0
"""
