class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dic = {}
        for i in range(len(nums)):
            if dic.has_key(nums[i]):
                dic[nums[i]] = 2
            else:
                dic[nums[i]] = 1
        for k, v in dic.items():
            if v == 1:
                return k
                
"""
# https://leetcode-cn.com/submissions/detail/73290377/

16 / 16 个通过测试用例
状态：通过
执行用时：32 ms
内存消耗：15.4 MB
"""
