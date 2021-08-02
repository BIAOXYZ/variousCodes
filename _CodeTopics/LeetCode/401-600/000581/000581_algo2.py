class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 答案一的思路：把数组分成三段，左右两段是即使整个数组排序也不会变的，中间那段是会变的。
        # 先把数组的副本排序，然后分别从左右两边开始核对。。。有点脑筋急转弯的味儿了- -

        nums2 = sorted(nums)
        length = len(nums)
        left, right = 0, length - 1

        while left < length - 1 and nums[left] == nums2[left]:
            left += 1
        if left == length - 1:
            return 0
        while nums[right] == nums2[right]:
            right -= 1
        return right - left + 1
        
"""
https://leetcode-cn.com/submissions/detail/202564528/

307 / 307 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 14 MB

执行用时：32 ms, 在所有 Python 提交中击败了99.20%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了30.52%的用户
"""
