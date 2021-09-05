class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 递归写法 II：照应了另外一种非递归写法。

        def binary_search_inner(arr, target, left, right):
            # 另一种写法这里是： if left > right:
            if left >= right:
                return -1
            mid = left + (right - left) / 2
            if arr[mid] < target:
                return binary_search_inner(arr, target, mid+1, right)
            elif arr[mid] > target:
                # 另一种写法这里是： return binary_search_inner(arr, target, left, mid-1)
                return binary_search_inner(arr, target, left, mid)
            else:
                return mid
        
        # 另一种写法这里是： return binary_search_inner(nums, target, 0, len(nums)-1)
        return binary_search_inner(nums, target, 0, len(nums))
        
"""
https://leetcode-cn.com/submissions/detail/215643165/

46 / 46 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 14 MB

执行用时：24 ms, 在所有 Python 提交中击败了70.92%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了50.95%的用户
"""
