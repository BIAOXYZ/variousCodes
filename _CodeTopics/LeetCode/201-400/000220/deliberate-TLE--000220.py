class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        # trivial的实现，遍历穷举（其实我觉得这个按道理是不应该超时的，除非k特别大）。
        # 看了一眼k，和数组长度一个级别，那估计要超时了？。。。

        length = len(nums)
        for i in range(length):
            leftBoundary, rightBoundary = i - 1, i + 1
            while leftBoundary >= max(0, i - k):
                if abs(nums[i] - nums[leftBoundary]) <= t:
                    return True
                leftBoundary -= 1
            while rightBoundary <= min(length - 1, i + k):
                if abs(nums[i]- nums[rightBoundary]) <= t:
                    return True
                rightBoundary += 1
        return False
        
"""
https://leetcode-cn.com/submissions/detail/168860808/

51 / 54 个通过测试用例
状态：超出时间限制
"""
