class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def map_num(num):
            l = list(str(num))
            l = [str(mapping[int(digit)]) for digit in l]
            return int(''.join(l))
        
        nums2 = [[map_num(num), i] for i, num in enumerate(nums)]
        nums2.sort()
        return [nums[ind] for _, ind in nums2]
    
"""
https://leetcode-cn.com/submissions/detail/277914784/

66 / 66 个通过测试用例
状态：通过
执行用时: 1740 ms
内存消耗: 21.7 MB
"""
