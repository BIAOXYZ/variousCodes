class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        length1, length2 = len(nums1), len(nums2)
        if length1 == 0 or length2 == 0:
            return []
        
        res = []
        for i in range(length1):
            if nums1[i] not in nums2:
                continue
            else:
                res.append(nums1[i])
                nums2.pop(nums2.index(nums1[i]))
        return res
        
"""
# https://leetcode-cn.com/submissions/detail/77685048/

61 / 61 个通过测试用例
状态：通过
执行用时：56 ms
内存消耗：12.7 MB
"""
