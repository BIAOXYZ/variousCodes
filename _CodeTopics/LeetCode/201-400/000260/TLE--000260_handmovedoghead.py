class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 手动狗头题
        return filter(lambda k : collections.Counter(nums)[k] == 1, collections.Counter(nums).keys())
        
"""
https://leetcode-cn.com/submissions/detail/233657136/

31 / 32 个通过测试用例
状态：超出时间限制
"""
