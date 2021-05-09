class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        len1, len2 = len(nums1), len(nums2)
        maxDis = 0
        
        for i in range(len1):
            for j in range(i, len2):
                if nums2[j] >= nums1[i]:
                    if j != len2 - 1:
                        continue
                    else:
                        maxDis = max(maxDis, j - i)
                        break
                else:
                    maxDis = max(maxDis, j - 1 - i)
                    break
        return maxDis
    
"""
https://leetcode-cn.com/submissions/detail/175688272/

20 / 30 个通过测试用例
状态：超出时间限制
"""
