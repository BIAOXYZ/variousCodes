class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dic = dict() # 等价于dic = {}
        for i in range(len(nums)):
            if dic.has_key(nums[i]):
                return True
            else:
                dic[nums[i]] = i
        return False
        
"""
# https://leetcode-cn.com/submissions/detail/73279458/

18 / 18 个通过测试用例
状态：通过
执行用时：44 ms
内存消耗：18.5 MB
"""
