class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        while val in nums:
            nums.pop(nums.index(val))
        return len(nums)
        
"""
https://leetcode-cn.com/submissions/detail/124533199/

113 / 113 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.9 MB

执行用时：24 ms, 在所有 Python 提交中击败了39.52%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了21.33%的用户
"""
