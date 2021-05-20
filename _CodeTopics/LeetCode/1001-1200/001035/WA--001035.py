class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        # 应该就是贪心思想 + 二重循环

        len1, len2 = len(nums1), len(nums2)
        curr1 = curr2 = 0
        res = 0
        
        while curr1 < len1:
            for i in range(curr2, len2):
                if nums2[i] == nums1[curr1]:
                    res += 1
                    curr2 = i + 1
                    break
            curr1 += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/179424481/

39 / 74 个通过测试用例
状态：解答错误

最后执行的输入：
[1,1,2,1,2]
[1,3,2,3,1]
"""
