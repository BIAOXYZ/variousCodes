class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:

        nums1.sort()
        nums2.sort()
        for num in nums1:
            if num in nums2:
                return num
        return min(nums1[0] * 10 + nums2[0], nums2[0] * 10 + nums1[0])
        
"""
https://leetcode.cn/problems/form-smallest-number-from-two-digit-arrays/submissions/463343910/?envType=daily-question&envId=2023-09-05

时间
详情
44ms
击败 58.29%使用 Python3 的用户
内存
详情
15.70MB
击败 28.88%使用 Python3 的用户
"""
