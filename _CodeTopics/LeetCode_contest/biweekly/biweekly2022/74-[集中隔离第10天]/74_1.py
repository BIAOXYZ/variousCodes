class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        ctr = Counter(nums)
        for v in ctr.values():
            if v & 1 == 1:
                return False
        return True
    
"""
https://leetcode-cn.com/submissions/detail/286022778/

132 / 132 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.4 MB
"""
