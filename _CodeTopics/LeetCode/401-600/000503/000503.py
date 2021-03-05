class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums:
            return []
        
        biggest = max(nums)
        length = len(nums)
        res = []
        for i in range(length):
            if nums[i] == biggest:
                res.append(-1)
            else:
                for j in range(i + 1, i + length):
                    if nums[j % length] > nums[i]:
                        res.append(nums[j % length])
                        break
        return res
        
"""
https://leetcode-cn.com/submissions/detail/151580774/

224 / 224 个通过测试用例
状态：通过
执行用时: 8812 ms
内存消耗: 14.7 MB

执行用时：8812 ms, 在所有 Python 提交中击败了5.00%的用户
内存消耗：14.7 MB, 在所有 Python 提交中击败了89.50%的用户
"""
