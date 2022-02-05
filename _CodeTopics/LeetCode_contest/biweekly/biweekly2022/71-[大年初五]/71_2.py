class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        
        small, equal, large = [], [], []
        for num in nums:
            if num < pivot:
                small.append(num)
            elif num > pivot:
                large.append(num)
            else:
                equal.append(num)
        return small + equal + large
    
"""
https://leetcode-cn.com/submissions/detail/265024445/

44 / 44 个通过测试用例
状态：通过
执行用时: 168 ms
内存消耗: 29.5 MB
"""
