class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        length = len(nums)
        if target <= nums[0]:
            return 0
        if target >= nums[-1]:
            return length

        # 先用左闭右闭的方式
        left, right = 0, length-1
        
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        # 如果while循环里没找到正确的结果，最后肯定是left > right了。而前一步肯定还满足
        # left <= right，移动了一下过了，说明要找的值介于移动后的新的（较大的）left和
        # （较小的）right之间。
        return left
        
"""
https://leetcode-cn.com/submissions/detail/88679635/

57 / 62 个通过测试用例
状态：解答错误

输入：[1,3]
      3
输出：2
预期：1
"""
