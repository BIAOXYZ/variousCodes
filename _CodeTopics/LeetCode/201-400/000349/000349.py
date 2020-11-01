class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        res = []
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in res:
                res.append(nums1[i])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/120265309/

60 / 60 个通过测试用例
状态：通过
执行用时: 48 ms
内存消耗: 13.2 MB

执行用时：48 ms, 在所有 Python 提交中击败了26.07%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了9.55%的用户
"""
