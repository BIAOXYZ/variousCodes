class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)

        # 采用不断交换位置的方法。
        for i in range(length):
            # 为避免死循环，一旦某个潜在位置上的值已经等于要被换过去的值，就不交换了。
            while nums[i] >= 1 and nums[i] <= length and nums[nums[i]-1] != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1
        
"""
https://leetcode-cn.com/submissions/detail/82477484/

165 / 165 个通过测试用例
状态：通过
执行用时：24 ms
内存消耗：12.6 MB
"""
