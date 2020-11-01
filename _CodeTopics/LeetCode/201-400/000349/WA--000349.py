class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        """
        # 这个是重复元素会多次计算在内的版本。
        res = []
        for i in range(len(nums1)-1):
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.remove(nums1[i])
        return res
        """

        res = []
        for i in range(len(nums1)-1):
            if nums1[i] in nums2 and nums1[i] not in res:
                res.append(nums1[i])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/120265212/

45 / 60 个通过测试用例
状态：解答错误

输入：
[1]
[1]
输出：
[]
预期：
[1]
"""
