class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        while val in nums:
            nums.remove(val)
        return len(nums)
        
"""
https://leetcode-cn.com/submissions/detail/124533332/

113 / 113 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13 MB

执行用时：20 ms, 在所有 Python 提交中击败了67.51%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了13.07%的用户
"""
