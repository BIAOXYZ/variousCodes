class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 手动狗头题
        return sorted(set(nums))[-3] if len(set(nums)) >= 3 else sorted(set(nums))[-1]
        
"""
https://leetcode-cn.com/submissions/detail/226159332/

31 / 31 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 14 MB

执行用时：20 ms, 在所有 Python 提交中击败了60.15%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了7.01%的用户
"""
