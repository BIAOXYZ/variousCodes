class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        res, currMax = nums[0], dic[nums[0]]
        for k, v in dic.items():
            if v > currMax:
                currMax = v
                res = k
        return res
        
"""
https://leetcode-cn.com/submissions/detail/124533683/

46 / 46 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 14.1 MB

执行用时：28 ms, 在所有 Python 提交中击败了77.74%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了29.21%的用户
"""
