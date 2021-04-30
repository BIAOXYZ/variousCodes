class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ctr = collections.Counter(nums)
        for k, v in ctr.items():
            if v == 1:
                return k
        
"""
https://leetcode-cn.com/submissions/detail/173488848/

14 / 14 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 14.9 MB

执行用时：28 ms, 在所有 Python 提交中击败了43.75%的用户
内存消耗：14.9 MB, 在所有 Python 提交中击败了5.08%的用户
"""
