class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        # 只需 n-1 轮循环即可。
        for i in range(n - 1):
            # 在第 i 轮（此处i包括0）循环中，走到倒数第 n-2-i 个位置即可。
            for j in range(n - 1 - i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
        
"""
https://leetcode-cn.com/submissions/detail/105802419/

10 / 11 个通过测试用例
状态：超出时间限制
"""
