class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i, num in enumerate(nums):
            if i == num % 10:
                return i
        return -1
    
"""
https://leetcode-cn.com/submissions/detail/233962596/

439 / 663 个通过测试用例
状态：解答错误
"""
"""
低级错误，不需要记录错误用例了。
"""
