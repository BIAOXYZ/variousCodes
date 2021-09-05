class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 第二种常见写法

        length = len(nums)
        # 第一种里是： left, right = 0, length-1
        left, right = 0, length
        
        # 第一种里是： while left <= right:
        while left < right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                # 第一种里是： right = mid - 1
                right = mid
            else:
                return mid
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/215642527/

46 / 46 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 14 MB

执行用时：20 ms, 在所有 Python 提交中击败了91.20%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了36.90%的用户
"""
