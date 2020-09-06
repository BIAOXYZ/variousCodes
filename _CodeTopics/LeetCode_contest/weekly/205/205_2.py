class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        len1, len2 = len(nums1), len(nums2)
        
        ht1, ht2 = {}, {}
        diagonal1, diagonal2 = [], []
        
        for i in range(len1):
            diagonal1.append(nums1[i] * nums1[i])
            for j in range(i):
                tmp = nums1[i] * nums1[j]
                if ht1.has_key(tmp):
                    ht1[tmp] += 1
                else:
                    ht1[tmp] = 1
        for i in range(len2):
            diagonal2.append(nums2[i] * nums2[i])
            for j in range(i):
                tmp = nums2[i] * nums2[j]
                if ht2.has_key(tmp):
                    ht2[tmp] += 1
                else:
                    ht2[tmp] = 1
        
        # print ht1
        # print ht2
        # print diagonal1
        # print diagonal2
        
        res = 0
        for elem in diagonal1:
            if ht2.has_key(elem):
                res += ht2[elem]
        for elem in diagonal2:
            if ht1.has_key(elem):
                res += ht1[elem]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/105238352/

92 / 92 个通过测试用例
状态：通过
执行用时: 496 ms
内存消耗: 32.3 MB
"""
