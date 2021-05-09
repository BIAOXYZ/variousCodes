import bisect
class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        len1, len2 = len(nums1), len(nums2)
        maxDis = 0
        nums2.reverse()
        
        for i in range(len1):
            if i >= len2:
                break
            j = bisect.bisect_left(nums2, nums1[i], 0, len2 - i)
            if j <= len2 - i:
                maxDis = max(maxDis, len2 - i - 1 - j)       
        return maxDis
    
"""
https://leetcode-cn.com/submissions/detail/175710821/

30 / 30 个通过测试用例
状态：通过
执行用时: 236 ms
内存消耗: 23.7 MB
"""
