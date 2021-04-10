class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 这题的技巧点主要在于数组 nums 经过旋转后，会形成以最小值为“低谷”的两个递增区间，举例如下：
        # [3,4,5,1,2]就是 3，4，5是左半边递增区间，1，2是右半边递增区间。二分查找时，根据 mid 的情况
        # 判断它在哪一个半边递增区间，从而相应的左移right 或者 右移left。

        if len(nums) < 3:
            return min(nums)
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) / 2
            if mid == 0:
                if nums[mid] < nums[mid+1] and nums[mid] < nums[-1]:
                    return nums[mid]
            elif mid == len(nums) - 1:
                if nums[mid] < nums[mid-1] and nums[mid] < nums[0]:
                    return nums[mid]
            else:
                if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                    return nums[mid]
                else:
                    # 此时 mid 在左半边递增区间，最小值在 mid 的右边，应该使 mid 向右移动，所以 left 要增加。
                    if nums[mid] > nums[-1]:
                        left = mid + 1
                    # 此时 mid 在右半边递增区间，最小值在 mid 的左边，应该使 mid 向左移动，所以 right 要减少。
                    elif nums[mid] < nums[-1]:
                        right = mid - 1
        return nums[mid]
        
"""
https://leetcode-cn.com/submissions/detail/166037269/

12 / 150 个通过测试用例
状态：超出时间限制

最后执行的输入：
[5,1,2,3,4]
"""
