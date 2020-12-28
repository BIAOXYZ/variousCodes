class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        dic = {}
        for num in nums:
            if dic.has_key(num):
                dic[num] += 1
            else:
                dic[num] = 1
        
        nums2 = dic.keys()
        nums2.sort()
        length = len(nums2)
        left, right = 0, length - 1
        
        res = 0
        while left < right:
            if nums2[left] + nums2[right] > k:
                right -= 1
            elif nums2[left] + nums2[right] < k:
                left += 1
            else:
                res += min(dic[nums2[left]], dic[nums2[right]])
                left += 1
                right -= 1
        if nums2[left] == nums2[right]:
            if nums2[left] + nums2[right] == k:
                res += dic[nums2[left]] / 2
        return res
    
"""
https://leetcode-cn.com/submissions/detail/128933449/

51 / 51 个通过测试用例
状态：通过
执行用时: 144 ms
内存消耗: 19.7 MB
"""
