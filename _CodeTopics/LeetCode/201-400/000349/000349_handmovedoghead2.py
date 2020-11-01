class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # 手动狗头题2
        return list(set(nums1) & set(nums2))
        
"""
https://leetcode-cn.com/submissions/detail/120265573/

60 / 60 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.5 MB

执行用时：24 ms, 在所有 Python 提交中击败了98.93%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了5.00%的用户
"""
