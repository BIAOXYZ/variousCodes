class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 手动狗头一把
        return sum(sorted(nums)[::2])
        
"""
https://leetcode-cn.com/submissions/detail/145970644/

83 / 83 个通过测试用例
状态：通过
执行用时: 68 ms
内存消耗: 14.7 MB

执行用时：68 ms, 在所有 Python 提交中击败了62.76%的用户
内存消耗：14.7 MB, 在所有 Python 提交中击败了8.67%的用户
"""
