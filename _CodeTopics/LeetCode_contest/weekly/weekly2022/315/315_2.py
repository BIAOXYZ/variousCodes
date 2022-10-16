class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        tmp = []
        for num in nums:
            tmp.append(int(str(num)[::-1]))
        return len(set(nums+tmp))
    
"""
https://leetcode.cn/submissions/detail/373421393/

44 / 44 个通过测试用例
状态：通过
执行用时: 244 ms
内存消耗: 37.1 MB
"""
