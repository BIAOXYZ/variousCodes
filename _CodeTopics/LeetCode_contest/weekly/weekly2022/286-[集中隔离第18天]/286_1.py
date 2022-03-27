class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        res = [[],[]]
        se1, se2 = set(nums1), set(nums2)
        used = set()
        for num in nums1:
            if num not in se2 and num not in used:
                res[0].append(num)
                used.add(num)
        used.clear()
        for num in nums2:
            if num not in se1 and num not in used:
                res[1].append(num)
                used.add(num)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/290066402/

202 / 202 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 13.6 MB
"""
