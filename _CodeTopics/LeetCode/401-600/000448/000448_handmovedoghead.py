class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 手动狗头一把。
        return set(range(1, len(nums)+1)) - set(nums)
        
"""
https://leetcode-cn.com/submissions/detail/145549217/

34 / 34 个通过测试用例
状态：通过
执行用时: 300 ms
内存消耗: 23.9 MB

执行用时：300 ms, 在所有 Python 提交中击败了98.94%的用户
内存消耗：23.9 MB, 在所有 Python 提交中击败了6.98%的用户
"""
