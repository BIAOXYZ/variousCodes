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
                res += dic[nums2[left] / 2]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/128932871/

3 / 51 个通过测试用例
状态：执行出错

执行出错信息：
Line 33: KeyError: 0
最后执行的输入：
[3,5,1,5]
2
"""
"""
纯属倒数第二行代码失误（除2肯定是取字典里的值然后除2，而不是用字典的key去除2），可以不用记录其实。
"""
