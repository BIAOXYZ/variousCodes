import bisect
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 最早出现在 LC454，不过这题作为模板题，放这儿更好。

        # 但是为了不改变下面这俩函数，待查找集合为空的情况是在外面处理的。
        # 一会写一个新的更general的在里面处理的。
        def binary_search_leftmost_equal(arr, x):
            i = bisect.bisect_left(arr, x)
            if i != len(arr) and arr[i] == x:
                return i
            else:
                return -1
        def binary_search_rightmost_equal(arr, x):
            i = bisect.bisect_right(arr, x)
            if i < len(arr) + 1 and arr[i-1] == x:
                return i-1
            else:
                return -1
        
        if not nums:
            return [-1, -1]
        return [binary_search_leftmost_equal(nums, target), binary_search_rightmost_equal(nums, target)]
        
"""
https://leetcode-cn.com/submissions/detail/127555188/

88 / 88 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.4 MB

执行用时：24 ms, 在所有 Python 提交中击败了45.07%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了22.11%的用户
"""
