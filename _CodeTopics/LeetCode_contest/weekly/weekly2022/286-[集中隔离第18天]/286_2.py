class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 1:
            return 1
        
        res = 0
        ptr1, ptr2 = 0, 1
        while ptr2 < n:
            if nums[ptr1] == nums[ptr2] and (ptr1 - res) & 1 == 0:
                res += 1
                ptr2 += 1
                while ptr2 < n and nums[ptr1] == nums[ptr2]:
                    res += 1
                    ptr2 += 1
            else:
                ptr1 = ptr2
                ptr2 += 1
        return res if (n - res) & 1 == 0 else res + 1
    
"""
https://leetcode-cn.com/submissions/detail/290123380/

114 / 114 个通过测试用例
状态：通过
执行用时: 116 ms
内存消耗: 22 MB
"""
