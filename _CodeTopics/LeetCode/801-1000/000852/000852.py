class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # 连续第三天二分查找。。。

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        
"""
https://leetcode-cn.com/submissions/detail/186697775/

34 / 34 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 14 MB

执行用时：24 ms, 在所有 Python 提交中击败了48.41%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了12.10%的用户
"""
