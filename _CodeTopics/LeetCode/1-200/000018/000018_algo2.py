class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        length = len(nums)
        res = []
        nums.sort()
        
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                end = length - 1
                for start in range(j+1, length):
                    if start > j+1 and nums[start] == nums[start-1]:
                        continue
                    while start < end and nums[i] + nums[j] + nums[start] + nums[end] > target:
                        end -= 1
                    if start == end:
                        break
                    if nums[i] + nums[j] + nums[start] + nums[end] == target:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/113534139/

283 / 283 个通过测试用例
状态：通过
执行用时: 844 ms
内存消耗: 12.3 MB

执行用时：844 ms, 在所有 Python 提交中击败了24.95%的用户
内存消耗：12.3 MB, 在所有 Python 提交中击败了93.97%的用户
"""
