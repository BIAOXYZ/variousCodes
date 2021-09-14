class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 脑筋急转弯 + 手动狗头
        return nums.index(max(nums))
        
"""
https://leetcode-cn.com/submissions/detail/219385352/

63 / 63 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB

执行用时：16 ms, 在所有 Python 提交中击败了72.87%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了72.63%的用户
"""
