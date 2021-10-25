class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        dic = {}
        for i, num in enumerate(nums2):
            dic[num] = -1
            for j in range(i+1, len(nums2)):
                if nums2[j] > num:
                    dic[num] = nums2[j]
                    break
        return [dic[num] for num in nums1]
        
"""
https://leetcode-cn.com/submissions/detail/232366531/

执行用时：36 ms, 在所有 Python 提交中击败了34.76%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了13.20%的用户
通过测试用例：
15 / 15
"""
